# Pipeline CLI — HubSpot

Pipeline de dados construído em Python para extração, transformação e exportação de deals do HubSpot.

Esse projeto foi desenvolvido como parte do meu plano de estudos em Engenharia de Dados. O objetivo foi construir um pipeline real, com dados reais da empresa, aplicando boas práticas de organização de código desde o início.

## O que o pipeline faz

1. **Extrai** deals diretamente da API do HubSpot via POST com filtro por `closedate`
2. **Transforma** filtrando apenas as campanhas válidas definidas no negócio
3. **Exporta** o resultado em `.xlsx` na pasta `output/`

## Estrutura do projeto

hubspot_cli/
├── extractor.py    → requisição na API com paginação
├── transformer.py  → filtro de campanhas válidas
├── reporter.py     → exportação em Excel
└── cli.py          → orquestrador do pipeline
tests/
├── conftest.py
└── test_transformer.py
.env                → credenciais (não versionado)
.gitignore

## Conceitos aplicados

- Requisições REST com `requests` — GET/POST, headers, body, paginação automática
- Autenticação via Bearer Token com variáveis de ambiente (`python-dotenv`)
- Separação de responsabilidades — cada módulo tem uma função única
- Testes unitários com `pytest` — validação do transformer com dados mock
- Segurança com `.env` no `.gitignore` — credenciais nunca versionadas

## Como executar

Instale as dependências:

```bash
pip install requests pandas openpyxl python-dotenv pytest
```

Crie um `.env` na raiz do projeto:

HUBSPOT_TOKEN=seu_token_aqui

Rode o pipeline completo:

```bash
python hubspot_cli/cli.py
```

Rode os testes:

```bash
pytest tests/ -v
```

## Resultado

O pipeline extrai os deals com `closedate >= 2025-01-01`, filtra pelas campanhas válidas e gera um arquivo `output/hubspot_deals.xlsx` pronto para análise.

## Próximos passos

- Orquestração com Apache Airflow
- Camadas Bronze / Prata / Ouro
- Expansão dos testes unitários
