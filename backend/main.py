# -*- coding: utf-8 -*-
"""
Main execution script for QWeather City Codes finder (Async version).
"""
import sys
import os
import csv
import time
import json
import asyncio
import aiohttp
from tqdm import tqdm

# Adicionar o diretório pai ao sys.path para permitir importações relativas se executado diretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.config import inicializar_ambiente
from backend.utils.text_utils import normalizar_texto, diferenca_minima
from backend.utils.geo_utils import get_estado_nome
from backend.services.api_service import buscar_cidade
from backend.services.ai_service import verificar_cidade_com_ia

# Controle de Concorrência
CONCURRENT_REQUESTS = 20  # Ajuste conforme limites da API e CPU

def carregar_cidades_processadas(csv_output):
    """Carrega as cidades que já foram processadas."""
    cidades_encontradas = set()
    try:
        with open(csv_output, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Pular cabeçalho
            for row in reader:
                if len(row) > 1 and row[1]:
                    cidade_estado = f"{row[1]},{row[4]}"
                    cidades_encontradas.add(cidade_estado)
    except FileNotFoundError:
        pass
    return cidades_encontradas

def adicionar_cidade_ao_csv(location, csv_output):
    """Adiciona uma cidade ao arquivo CSV (Synch wrapper para manter simplicidade no write)."""
    with open(csv_output, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            location.get("id", ""),
            location.get("name", ""), 
            "BR", "Brazil", 
            location.get("adm1", ""), 
            location.get("adm2", ""), 
            location.get("tz", ""), 
            location.get("lat", ""), 
            location.get("lon", "")
        ])

async def processar_municipio_async(idx, total_municipios, cidade, uf, row, status_col_index, linhas, api_key, cidades_encontradas, config, session, semaphore, progress_bar, use_ai=True, generate_file=False):
    """Processa um município de forma assíncrona."""
    csv_output, municipios_input = config
    
    async with semaphore:
        linha_idx = idx + 1
        
        # Verificar se processado com SUCESSO
        if "✓" in row[status_col_index]:
            progress_bar.update(1)
            return
        
        cidade_estado = f"{cidade},{get_estado_nome(uf)}"
        if cidade_estado in cidades_encontradas:
            linhas[linha_idx][status_col_index] = "✓"
            progress_bar.update(1)
            return

        try:
            response_data = await buscar_cidade(cidade, uf, api_key, session)
            status_code = response_data["status_code"]
            data = response_data["data"]
            
            if status_code == 200 and data.get("location"):
                match_found = False
                estado_correto_encontrado = False
                cidade_normalizada = normalizar_texto(cidade)
                
                # Primeira passada: Tentativa de Match Exato/Fuzzy simples
                for location in data["location"]:
                    if location.get("adm1", "").lower() == get_estado_nome(uf).lower():
                        estado_correto_encontrado = True
                        name_norm = normalizar_texto(location.get("name", ""))
                        adm2_norm = normalizar_texto(location.get("adm2", ""))
                        
                        if (name_norm == cidade_normalizada or adm2_norm == cidade_normalizada or
                            diferenca_minima(name_norm, cidade_normalizada) or
                            diferenca_minima(adm2_norm, cidade_normalizada)):
                            
                            match_found = True
                            adicionar_cidade_ao_csv(location, csv_output)
                            linhas[linha_idx][status_col_index] = "✓"
                            break
                
                # Se não achou match direto, mas tem cidades no estado --> IA / Manual
                if not match_found and estado_correto_encontrado:
                   estado_nome = get_estado_nome(uf).lower()
                   locations_estado = [loc for loc in data["location"] if loc.get("adm1", "").lower() == estado_nome]
                   
                   # Chama verificação com os parâmetros escolhidos pelo usuário
                   resultado_ia = await verificar_cidade_com_ia(cidade, get_estado_nome(uf), locations_estado, use_ai=use_ai, generate_file=generate_file)
                   
                   if resultado_ia["correspondencia"]:
                       for location in locations_estado:
                           if location.get("id") == resultado_ia["cidade_id"]:
                               adicionar_cidade_ao_csv(location, csv_output)
                               linhas[linha_idx][status_col_index] = "⚠️✓ - IA"
                               break
                   elif generate_file and "manual_file" in resultado_ia:
                       # Se gerou arquivo manual, marcamos no CSV
                       linhas[linha_idx][status_col_index] = "Verificar Manualmente (Prompt Gerado)"
                   else:
                       linhas[linha_idx][status_col_index] = "⚠️"

                elif not estado_correto_encontrado:
                     linhas[linha_idx][status_col_index] = "⚠️"
            
            elif status_code == 404:
                linhas[linha_idx][status_col_index] = "X"
            else:
                linhas[linha_idx][status_col_index] = f"Erro API: {status_code}"

        except Exception as e:
            linhas[linha_idx][status_col_index] = f"Erro: {str(e)}"
        
        progress_bar.update(1)

async def main_async():
    try:
        print("Iniciando processamento ASSÍNCRONO...")
        api_keys, csv_output, municipios_input = inicializar_ambiente()
        
        # Lógica de Modo Manual / IA / Arquivos
        ai_api_key = os.getenv("AI_API_KEY")
        use_ai = False
        generate_file = False
        
        # 1. Pergunta sobre uso da IA
        if ai_api_key:
            print("\n[CONFIG] Chave de API de IA detectada.")
            resp_ai = input("Deseja utilizar a IA para verificar ambiguidades? (S/n): ").strip().lower()
            if resp_ai != 'n':
                use_ai = True
        else:
            print("\n[AVISO] Chave de API de IA não encontrada. IA será desativada.")
        
        # 2. Pergunta sobre geração de arquivos
        resp_file = input("Deseja gerar arquivos de texto para verificação manual dos casos ambíguos? (s/N): ").strip().lower()
        if resp_file == 's':
            generate_file = True
            
        print(f"\n[CONFIG] IA: {'ATIVADA' if use_ai else 'DESATIVADA'} | Arquivos Manuais: {'ATIVADO' if generate_file else 'DESATIVADO'}\n")
        
        config = (csv_output, municipios_input)
        cidades_encontradas = carregar_cidades_processadas(csv_output)
        
        municipios = []
        linhas = []
        
        with open(municipios_input, 'r', encoding='utf-8') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            linhas.append(header)
            
            status_col_index = -1
            if "STATUS_PROCESSAMENTO" in header:
                status_col_index = header.index("STATUS_PROCESSAMENTO")
            else:
                header.append("STATUS_PROCESSAMENTO")
                status_col_index = len(header) - 1
            
            for row in reader:
                if len(row) > 3:
                    uf = row[0]
                    nome_municipio = row[3].strip()
                    while len(row) <= status_col_index:
                        row.append("")
                    municipios.append((nome_municipio, uf, row))
                    linhas.append(row)
        
        total_municipios = len(municipios)
        semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            with tqdm(total=total_municipios, desc="Processando Cidades") as pbar:
                for idx, (cidade, uf, row) in enumerate(municipios):
                    # Round-robin API keys
                    api_key = api_keys[idx % len(api_keys)]
                    
                    task = processar_municipio_async(
                        idx, total_municipios, cidade, uf, row, 
                        status_col_index, linhas, api_key, 
                        cidades_encontradas, config, session, semaphore, pbar,
                        use_ai=use_ai, generate_file=generate_file
                    )
                    tasks.append(task)
                
                # Executar todas as tasks em chunks
                chunk_size = 50
                for i in range(0, len(tasks), chunk_size):
                    chunk = tasks[i:i + chunk_size]
                    await asyncio.gather(*chunk)
                    
                    # Salvar progresso
                    with open(municipios_input, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerows(linhas)
        
        print("\nProcessamento concluído!")
        
        # Gerar arquivo de erros (Filtrando erros de API 400/500/etc e mantendo apenas falhas reais ou IA)
        erros_output = os.path.join(os.path.dirname(municipios_input), "cidades_com_erro.csv")
        
        # Filtro: Ignora se tiver "✓", e ignora se começar com "Erro API"
        cidades_erro = []
        for row in linhas:
            if row == linhas[0]: continue # Header
            status = row[status_col_index]
            
            if "✓" in status: continue
            if str(status).startswith("Erro API"): continue # Ignora erros transientes da API QWeather
            
            cidades_erro.append(row)
        
        if cidades_erro:
            with open(erros_output, 'w', newline='', encoding='utf-8') as f_err:
                writer = csv.writer(f_err)
                writer.writerow(header)
                writer.writerows(cidades_erro)
            print(f"Arquivo de erros gerado: {erros_output}")
            print(f"Total de cidades para verificação: {len(cidades_erro)}")
        else:
            print("Nenhuma cidade com erro/pendência encontrada.")

        if generate_file:
            print("Verifique a pasta 'manual_verification' (dentro de 'data' ou pai) para os prompts gerados caso existam.")

    except Exception as e:
        print(f"Erro main: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main_async())
