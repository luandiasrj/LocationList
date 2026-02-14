# QWeather City Codes

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

[English](#english) | [Português](#português)

---

## Português

### Sobre o Projeto

Este repositório contém uma ferramenta para buscar códigos de cidades brasileiras na API QWeather. Esses códigos são necessários para configurar a previsão do tempo em relógios inteligentes chineses que utilizam a API QWeather.

### Funcionalidades

- **Script Python**: Busca códigos de cidades brasileiras na API QWeather e os salva em um arquivo CSV.
- **Interface Web**: Permite buscar códigos de cidades diretamente no navegador, sem necessidade de executar o script.
- **Base de Dados**: Inclui uma lista de cidades brasileiras com seus respectivos códigos QWeather.

### Significados dos Status/Erros no CSV

- **✓**: Processado com sucesso.
- **✓ (IA)**: Processado com sucesso com ajuda da IA.
- **⚠️ Sem correspondência no estado**: A API encontrou cidades com esse nome, mas nenhuma no estado (UF) correto. Pode exigir correção manual no nome.
- **IA: Sem correspondência**: A IA analisou mas não teve confiança suficiente. Requer verificação manual.
- **Verificar Manualmente (Prompt Gerado)**: O sistema gerou um arquivo de texto na pasta `manual_verification` para você checar.
- **Erro API: 400**: Requisição inválida (nome da cidade pode estar estranho).
- **Erro API: 500**: Erro interno do servidor da API (tente novamente mais tarde).

### Como Usar a Interface Web

1. Acesse a [página web](https://luandiasrj.github.io/qweather-city-codes/)
2. Digite o nome da cidade que você deseja buscar
3. Copie o código da cidade encontrada
4. Configure seu relógio usando o código obtido

### Como Executar o Script Python

Se você deseja executar o script Python para atualizar a base de dados ou buscar cidades específicas, siga os passos abaixo:

#### Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

#### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/luandiasrj/qweather-city-codes.git
   cd qweather-city-codes
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as chaves de API:
   - Crie um arquivo `.env` na raiz do projeto (veja `.env.example`)
   - Adicione suas chaves de API QWeather (obtenha em [dev.qweather.com](https://dev.qweather.com/))
   ```
   API_KEY_1="sua_chave_api_1"
   API_KEY_2="sua_chave_api_2"
   ```

#### Execução

Execute o script principal:
```bash
python -m backend.main
```

O script irá:
1. Ler o arquivo `data/municipios_brasileiros.csv` com a lista de municípios brasileiros
2. Buscar os códigos de cada cidade na API QWeather
3. Salvar os resultados no arquivo `docs/Brasil-City-List-latest.csv`

### Estrutura do Projeto

```
qweather-city-codes/
├── .env.example                # Exemplo de arquivo de ambiente
├── .gitignore                  # Git ignore file
├── LICENSE                     # Licença CC BY-NC 4.0
├── README.md                   # Documentação principal
├── requirements.txt            # Dependências Python
├── backend/                    # Código Python (backend)
│   ├── config.py               # Configurações do projeto
│   ├── main.py                 # Script principal (async)
│   ├── services/               # Serviços (API, IA)
│   └── utils/                  # Utilitários (texto, geo)
├── data/                       # Dados de entrada
│   └── municipios_brasileiros.csv
└── docs/                       # GitHub Pages (interface web)
    ├── index.html              # Interface web
    └── Brasil-City-List-latest.csv
```

### Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Licença

Este projeto está licenciado sob a licença **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Você é livre para compartilhar e adaptar este material, desde que:
- Dê os devidos créditos ao autor
- Não utilize o material para fins comerciais

---

## English

### About the Project

This repository contains a tool to find Brazilian city codes in the QWeather API. These codes are necessary to configure weather forecasts on Chinese smartwatches that use the QWeather API.

### Features

- **Python Script**: Searches for Brazilian city codes in the QWeather API and saves them to a CSV file.
- **Web Interface**: Allows searching for city codes directly in the browser, without needing to run the script.
- **Database**: Includes a list of Brazilian cities with their respective QWeather codes.

### How to Use the Web Interface

1. Access the [web page](https://luandiasrj.github.io/qweather-city-codes/)
2. Type the name of the city you want to search for
3. Copy the code of the found city
4. Configure your watch using the obtained code

### How to Run the Python Script

If you want to run the Python script to update the database or search for specific cities, follow the steps below:

#### Prerequisites

- Python 3.6 or higher
- Pip (Python package manager)

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/luandiasrj/qweather-city-codes.git
   cd qweather-city-codes
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys:
   - Create a `.env` file in the project root (see `.env.example`)
   - Add your QWeather API keys (get them at [dev.qweather.com](https://dev.qweather.com/))
   ```
   API_KEY_1="your_api_key_1"
   API_KEY_2="your_api_key_2"
   ```

#### Execution

Run the main script:
```bash
python -m backend.main
```

The script will:
1. Read the `data/municipios_brasileiros.csv` file with the list of Brazilian municipalities
2. Search for the codes of each city in the QWeather API
3. Save the results to the `docs/Brasil-City-List-latest.csv` file

### Project Structure

```
qweather-city-codes/
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore file
├── LICENSE                     # CC BY-NC 4.0 License
├── README.md                   # Main documentation
├── requirements.txt            # Python dependencies
├── backend/                    # Python code (backend)
│   ├── config.py               # Project configuration
│   ├── main.py                 # Main script (async)
│   ├── services/               # Services (API, AI)
│   └── utils/                  # Utilities (text, geo)
├── data/                       # Input data
│   └── municipios_brasileiros.csv
└── docs/                       # GitHub Pages (web interface)
    ├── index.html              # Web interface
    └── Brasil-City-List-latest.csv
```

### Contribution

Contributions are welcome! If you want to contribute to this project, follow the steps below:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License - see the [LICENSE](LICENSE) file for details.

You are free to share and adapt this material, as long as you:
- Give appropriate credit to the author
- Do not use the material for commercial purposes
