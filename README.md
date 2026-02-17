# QWeather City Codes

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

[English](#english) | [Português](#português)

---

## Português

### Sobre o Projeto

Este repositório contém uma ferramenta completa para gerenciar e consultar códigos de cidades da API QWeather, essenciais para configurar a previsão do tempo em relógios inteligentes (smartwatches) chineses baseados em ESP8266, especificamente para dispositivos **[GeekMagic](https://geekmagic.com/)** como o **[SmallTV-Pro](https://github.com/GeekMagicClock/smalltv-pro)**.

O projeto é dividido em duas partes principais:

1.  **Backend (Atualizador de Dados)**: Um conjunto de scripts Python que consulta a API da QWeather e usa Inteligência Artificial (Google Gemini) para identificar corretamente os códigos das cidades brasileiras, gerando uma base de dados precisa.
2.  **Frontend (Visualizador Web)**: Uma interface web estática (hospedada no GitHub Pages) que lê a base de dados gerada e permite que qualquer usuário pesquise facilmente o código de sua cidade.

### Funcionalidades

-   **Busca Inteligente**: Utiliza a API da QWeather e, em casos de dúvida, recorre ao Google Gemini para desambiguação de cidades.
-   **Interface Web Amigável**: Permite buscar códigos de cidades diretamente no navegador, sem necessidade de instalar nada.
-   **Base de Dados Otimizada**: Lista curada de cidades brasileiras com seus respectivos ID, coordenadas e fuso horário.
-   **Modo Híbrido**: O script de atualização pode operar de forma totalmente automática ou gerar arquivos para verificação manual em casos complexos.

### Significados dos Status no CSV (Backend)

Durante a geração da base de dados, o script classifica cada cidade:

-   **✓**: Processado com sucesso (Encontrado via API padrão).
-   **⚠️✓ - IA**: Processado com sucesso via IA (Google Gemini resolveu a ambiguidade).
-   **⚠️**: Atenção (Não encontrado pela IA ou sem correspondência exata no estado).
-   **X**: Não encontrada (Erro 404 - Cidade não existe na API QWeather).
-   **Verificar Manualmente**: O sistema gerou um arquivo na pasta `manual_verification` para análise humana.
-   **Erro API**: Falha na comunicação com a API.

### Como Usar a Interface Web (Para Usuários Finais)

Se você apenas quer o código para o seu relógio:

1.  Acesse a [página web do projeto](https://luandiasrj.github.io/LocationList/).
2.  Digite o nome da cidade (ex: "Niterói, RJ").
3.  Copie o código numérico exibido (ex: `11505`).
4.  Configure seu relógio usando este código.

### Como Executar o Script Python (Para Desenvolvedores/Manutenção)

Se você deseja atualizar a base de dados (`docs/Brasil-City-List-latest.csv`) ou contribuir com o código:

#### Pré-requisitos

-   Python 3.8 ou superior
-   Conta na QWeather (para obter chaves de API)
-   Conta no Google AI Studio (opcional, para uso da IA Gemini)

#### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/luandiasrj/LocationList.git
    cd LocationList
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure as chaves de API:
    -   Copie o arquivo de exemplo: `cp .env.example .env` (ou renomeie manualmente).
    -   Edite o arquivo `.env` e adicione suas chaves.
    
    Exemplo de `.env`:
    ```ini
    # Chave gratuita da QWeather (obrigatório)
    API_KEY_1="sua_chave_qweather_aqui"
    
    # Chave do Google Gemini (recomendado para melhor precisão)
    AI_API_KEY="sua_chave_google_ai_aqui"
    ```

#### Execução

Execute o script principal como um módulo:

```bash
python -m backend.main
```

O script irá:
1.  Ler a lista de municípios em `data/municipios_brasileiros.csv`.
2.  Consultar a API para cada cidade não processada.
3.  Salvar os resultados automaticamente em `docs/Brasil-City-List-latest.csv`.

### Estrutura do Projeto

```
LocationList/
├── .env.example                # Modelo de configuração de ambiente
├── backend/                    # Lógica do atualizador de dados
│   ├── main.py                 # Ponto de entrada (Async)
│   ├── config.py               # Configurações globais
│   └── services/               # Integrações (QWeather API, Google Gemini)
├── data/                       # Dados brutos (lista de municípios IBGE/outros)
├── docs/                       # Frontend estático (GitHub Pages)
│   ├── index.html              # Interface de busca
│   ├── script.js               # Lógica da interface web
│   └── Brasil-City-List-latest.csv # Base de dados final (gerada pelo backend)
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou Pull Requests.

### Licença

Este projeto está licenciado sob a licença **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## English

### About the Project

This repository hosts a comprehensive tool for managing and retrieving city codes from the QWeather API, which are required to configure weather forecasts on ESP8266-based Chinese smartwatches, specifically for **[GeekMagic](https://geekmagic.com/)** devices like the **[SmallTV-Pro](https://github.com/GeekMagicClock/smalltv-pro)**.

The project consists of two main parts:

1.  **Backend (Data Updater)**: A set of Python scripts that query the QWeather API and utilize Artificial Intelligence (Google Gemini) to correctly identify Brazilian city codes, generating an accurate database.
2.  **Frontend (Web Viewer)**: A static web interface (hosted on GitHub Pages) that reads the generated database, allowing any user to easily search for their city code.

### Features

-   **Smart Search**: Uses the QWeather API and, for ambiguous cases, leverages Google Gemini to resolve city matches.
-   **User-Friendly Web Interface**: Allows searching for city codes directly in the browser, no installation required.
-   **Optimized Database**: Curated list of Brazilian cities with their respective IDs, coordinates, and timezones.
-   **Hybrid Mode**: The update script can run fully automatically or generate files for manual verification in complex cases.

### CSV Status Meanings (Backend)

During database generation, the script classifies each city:

-   **✓**: Successfully processed (Found via standard API).
-   **⚠️✓ - IA**: Successfully processed via AI (Google Gemini resolved the ambiguity).
-   **⚠️**: Warning (Not found by AI or no exact match in the state).
-   **X**: Not found (Error 404 - City does not exist in QWeather API).
-   **Verificar Manualmente**: System generated a file in `manual_verification` folder for human review.
-   **Erro API**: Communication failure with the API.

### How to Use the Web Interface (For End Users)

If you just want the code for your watch:

1.  Go to the [project web page](https://luandiasrj.github.io/LocationList/).
2.  Type your city name (e.g., "Niterói, RJ").
3.  Copy the numeric code shown (e.g., `11505`).
4.  Configure your watch using this code.

### How to Run the Python Script (For Developers/Maintainers)

If you want to update the database (`docs/Brasil-City-List-latest.csv`) or contribute to the code:

#### Prerequisites

-   Python 3.8 or higher
-   QWeather Account (to get API keys)
-   Google AI Studio Account (optional, for Gemini AI features)

#### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/luandiasrj/LocationList.git
    cd LocationList
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure API keys:
    -   Copy the example file: `cp .env.example .env` (or rename manually).
    -   Edit `.env` and add your keys.
    
    Example `.env`:
    ```ini
    # QWeather Free Key (Required)
    API_KEY_1="your_qweather_key_here"
    
    # Google Gemini Key (Recommended for better accuracy)
    AI_API_KEY="your_google_ai_key_here"
    ```

#### Execution

Run the main script as a module:

```bash
python -m backend.main
```

The script will:
1.  Read the municipality list from `data/municipios_brasileiros.csv`.
2.  Query the API for each unprocessed city.
3.  Automatically save results to `docs/Brasil-City-List-latest.csv`.

### Project Structure

```
LocationList/
├── .env.example                # Environment configuration template
├── backend/                    # Data updater logic
│   ├── main.py                 # Entry point (Async)
│   ├── config.py               # Global settings
│   └── services/               # Integrations (QWeather API, Google Gemini)
├── data/                       # Raw data (IBGE municipality list)
├── docs/                       # Static Frontend (GitHub Pages)
│   ├── index.html              # Search interface
│   ├── script.js               # Web logic
│   └── Brasil-City-List-latest.csv # Final database (generated by backend)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

### Contribution

Contributions are welcome! Feel free to open Issues or Pull Requests.

### License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License.
See the [LICENSE](LICENSE) file for details.