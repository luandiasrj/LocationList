# -*- coding: utf-8 -*-
"""
Módulo de configuração e inicialização do ambiente.
"""
import os
import csv
from dotenv import load_dotenv

# Configurações globais - Ajustadas para a nova estrutura de diretórios
# Considerando que o script é executado a partir de 'backend/main.py'
# ou 'backend/' como diretório de trabalho, os caminhos precisam subir um nível
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_OUTPUT = os.path.join(BASE_DIR, "docs", "Brasil-City-List-latest.csv")
MUNICIPIOS_INPUT = os.path.join(BASE_DIR, "data", "municipios_brasileiros.csv")
MUNICIPIOS_INPUT = os.path.join(BASE_DIR, "data", "municipios_brasileiros.csv")

def inicializar_ambiente():
    """
    Inicializa o ambiente de execução, carregando variáveis de ambiente e criando diretórios.
    
    Returns:
        tuple: (list: api_keys, str: csv_output_path, str: municipios_input_path, str: resultados_ia_dir)
    """
    # Carregar variáveis de ambiente do arquivo .env na raiz do projeto
    env_path = os.path.join(BASE_DIR, ".env")
    load_dotenv(env_path)
    
    # Obter chaves de API do arquivo .env
    api_keys = []
    for i in range(1, 6):  # Assumindo que existem 5 chaves
        key = os.getenv(f"API_KEY_{i}")
        if key:
            api_keys.append(key)
    
    if not api_keys:
        # Tentar procurar apenas API_KEY se as numeradas não existirem
        key = os.getenv("API_KEY")
        if key:
            api_keys.append(key)
        else:
            raise ValueError("Nenhuma chave de API encontrada no arquivo .env")
    
    # Inicializar arquivo de saída se não existir
    if not os.path.exists(CSV_OUTPUT):
        # Garantir que o diretório de saída existe
        os.makedirs(os.path.dirname(CSV_OUTPUT), exist_ok=True)
        with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                "Location_ID", "Location_Name_PT", "ISO_3166_1",
                "Country_Region_PT", "Adm1_Name_PT", 
                "Adm2_Name_PT", "Timezone", "Latitude", "Longitude"
            ])
    
    return api_keys, CSV_OUTPUT, MUNICIPIOS_INPUT
