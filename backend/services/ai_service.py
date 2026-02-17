import time
import os
import json
import re
import asyncio
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Configurações de Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATS_FILE = os.path.join(DATA_DIR, "ai_model_stats.json")

# Lista de prioridade será populada dinamicamente
MODELOS_PRIORIDADE = []

# Mapeia modelo para o timestamp em que poderá ser usado novamente
MODEL_BACKOFFS = {}

# Índice do modelo atualmente preferido (O último que deu certo)
CURRENT_MODEL_INDEX = 0

MODEL_LOCK = asyncio.Lock()

def load_model_stats():
    """Carrega estatísticas persistentes dos modelos."""
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_model_stats(stats):
    """Salva estatísticas persistentes dos modelos."""
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
    except Exception as e:
        print(f"[IA] Erro ao salvar stats: {e}")

def get_model_score(model_name, stats=None):
    """Calcula pontuação para ordenação: Sucesso > Versão > Tier."""
    name = model_name.lower()
    version = 0.0
    
    # Extrair versão
    match = re.search(r'gemini-(\d+(\.\d+)?)', name)
    if match:
        version = float(match.group(1))
    else:
        if "latest" in name: version = 1.5 
    
    tier = 0.5
    if "ultra" in name: tier = 3
    elif "pro" in name: tier = 2
    elif "flash" in name: tier = 1
    elif "nano" in name or "lite" in name: tier = 0
    
    # Penalizar modelos de imagem/audio puro
    if "vision" in name or "audio" in name: tier -= 0.5
    
    # Bônus por Histórico de Sucesso (Winner-Stays)
    success_bonus = 0
    penalty = 0
    if stats and model_name in stats:
        s = stats[model_name]
        success_bonus = s.get("success_count", 0) * 50 # Peso alto para o que funciona
        penalty = s.get("hard_error_count", 0) * 200    # Penalidade severa para 429 persistentes
        
    return (success_bonus - penalty) + (version * 10) + tier

async def async_visual_wait(seconds):
    """Espera visual com contagem regressiva (mesma linha)."""
    if seconds <= 0: return
    print(f"[IA] Aguardando liberação de cota por {seconds:.1f}s...")
    for i in range(int(seconds), 0, -1):
        print(f"[IA] Aguardando... {i}s restantes   \r", end="", flush=True)
        await asyncio.sleep(1)
    print(f"[IA] Retomando processamento...               ", flush=True)

async def verificar_cidade_com_ia(cidade, estado, locations, use_ai=True, generate_file=False):
    """
    Usa a API do Google Generative AI para verificar se alguma das localizações corresponde à cidade procurada.
    Implementa estratégia de Winner-Stays e detecção de cota zerada.
    """
    global CURRENT_MODEL_INDEX
    
    print(f"Verificação: '{cidade}' ({estado}). AI={use_ai}, File={generate_file}")
    
    ai_api_key = os.getenv("AI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    # Prepara o prompt (usado tanto para IA quanto para arquivo)
    prompt = f"""
    Objetivo: Identificar se algum dos candidatos abaixo corresponde à cidade brasileira:
    Cidade Alvo: "{cidade}"
    Estado Alvo: "{estado}"
    Candidatos: {json.dumps(locations, ensure_ascii=False)}
    
    Responda APENAS JSON:
    {{
      "correspondencia": true/false,
      "cidade_id": "ID",
      "explicacao": "justificativa"
    }}
    """

    # Geração de Arquivo Manual (Se solicitado)
    if generate_file:
        manual_dir = os.path.join(os.path.dirname(DATA_DIR), "manual_verification")
        os.makedirs(manual_dir, exist_ok=True)
        filename = f"verify_{normalizar_texto(cidade)}_{normalizar_texto(estado)}.txt"
        filepath = os.path.join(manual_dir, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"CIDADE: {cidade} - {estado}\n")
                f.write("-" * 50 + "\n")
                f.write(prompt)
                f.write("\n" + "-" * 50 + "\n")
                f.write("AÇÃO NECESSÁRIA: Verifique manualmente e atualize o CSV se encontrar o ID correto.\n")
        except Exception as e:
            print(f"[IA] Erro ao gerar arquivo manual: {e}")

    # Lógica de Decisão AI vs Manual
    if not use_ai:
        return {
            "correspondencia": False, 
            "cidade_id": "", 
            "explicacao": "IA desativada pelo usuário.",
            "manual_file": generate_file 
        }
    
    if not ai_api_key:
        print("[IA] Chave de API ausente. Retornando sem consulta.")
        return {"correspondencia": False, "cidade_id": "", "explicacao": "Chave da API não configurada", "manual_file": generate_file}

    stats = load_model_stats()

    generation_config = genai.types.GenerationConfig(temperature=0.1, response_mime_type="application/json")

    while True:
        current_model_idx = CURRENT_MODEL_INDEX
        model_name = MODELOS_PRIORIDADE[current_model_idx % len(MODELOS_PRIORIDADE)]
        now = time.time()
        
        # Verificar Backoff
        if now < MODEL_BACKOFFS.get(model_name, 0):
            print(f"[IA] {model_name} em cota. Pulando... (Livre em {MODEL_BACKOFFS[model_name]-now:.1f}s)")
            found_free = False
            for i in range(len(MODELOS_PRIORIDADE)):
                test_idx = (current_model_idx + i) % len(MODELOS_PRIORIDADE)
                test_model = MODELOS_PRIORIDADE[test_idx]
                if now >= MODEL_BACKOFFS.get(test_model, 0):
                    async with MODEL_LOCK: CURRENT_MODEL_INDEX = test_idx
                    model_name = test_model
                    found_free = True
                    break
            
            if not found_free:
                earliest_ready = min(MODEL_BACKOFFS.values())
                await async_visual_wait(max(0.1, earliest_ready - now))
                continue

        model = genai.GenerativeModel(model_name, system_instruction="Especialista em geografia do Brasil.")
        
        try:
            response = await model.generate_content_async(prompt, generation_config=generation_config)
            resultado = json.loads(response.text)
            
            # Registrar SUCESSO e Pinar Modelo
            print(f"[IA] Sucesso com {model_name}.")
            if model_name not in stats: stats[model_name] = {"success_count": 0, "hard_error_count": 0}
            stats[model_name]["success_count"] += 1
            save_model_stats(stats)
            return resultado

        except Exception as e:
            error_str = str(e)
            print(f"[IA] Erro {model_name}: {error_str[:200]}...")
            
            if "429" in error_str or "ResourceExhausted" in error_str:
                # Detecção de Cota Realmente Esgotada (Limit: 0)
                wait_time = 30
                match = re.search(r'retry in (\d+(\.\d+)?)s', error_str)
                if match: wait_time = float(match.group(1)) + 1
                
                if "limit: 0" in error_str.lower():
                    print(f"[IA] COTA ZERADA detectada em {model_name}. Bloqueando por 24h.")
                    wait_time = 86400 # 24 horas
                    if model_name not in stats: stats[model_name] = {"success_count": 0, "hard_error_count": 0}
                    stats[model_name]["hard_error_count"] += 1
                    save_model_stats(stats)

                MODEL_BACKOFFS[model_name] = time.time() + wait_time
                async with MODEL_LOCK: CURRENT_MODEL_INDEX = (CURRENT_MODEL_INDEX + 1) % len(MODELOS_PRIORIDADE)
                continue

            # Erro 404 (Modelo Removido/Indisponível)
            if "404" in error_str or "not found" in error_str.lower():
                MODEL_BACKOFFS[model_name] = time.time() + 86400
                async with MODEL_LOCK: CURRENT_MODEL_INDEX = (CURRENT_MODEL_INDEX + 1) % len(MODELOS_PRIORIDADE)
                continue

            # Outros erros -> Tenta próximo
            async with MODEL_LOCK: CURRENT_MODEL_INDEX = (CURRENT_MODEL_INDEX + 1) % len(MODELOS_PRIORIDADE)
            await asyncio.sleep(1)
            continue
