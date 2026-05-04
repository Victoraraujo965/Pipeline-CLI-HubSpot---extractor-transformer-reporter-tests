import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

TOKEN = os.getenv('HUBSPOT_TOKEN')
CAMINHO_BASE = "https://api.hubapi.com"
TAMANHO_PAGINAS = 100
OBJETO = "deals"
LIMITE_PAGINAS = None
PROPIEDADES = ['id', 'id_original', 'acao']


def fazer_requisicao(OBJETO, PROPIEDADES=None, LIMITE_PAGINAS=None):
    """Função para requisição básica no Hub"""
    headers = {
        'Authorization': f"Bearer {TOKEN}",
        'Content-Type': 'application/json'
    }

    body = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "closedate",
                        "operator": "GTE",
                        "value": "2025-01-01"
                    }
                ]
            }
        ],
        "properties": PROPIEDADES,
        "limit": TAMANHO_PAGINAS
    }

    todos_resultados = []

    while True:
        try:
           
            filtro = requests.post(
                f"{CAMINHO_BASE}/crm/v3/objects/{OBJETO}/search",
                headers=headers,
                json=body
            )
            
            filtro.raise_for_status()
            
            data = filtro.json()
            
            resultado = data.get("results")
            
            todos_resultados.extend(resultado)
            
            print(f"Página coletada: {len(todos_resultados)} registros até agora")
            
            proximo = data.get("paging", {}).get("next", {}).get("after")
            
            if proximo is None:
            
                break
            
            body["after"] = proximo

        except requests.exceptions.HTTPError as e:
            
            print(f"Erro na requisição: {e}")
            
            break

    df_o = pd.DataFrame(todos_resultados)
    df_T = pd.json_normalize(df_o["properties"])
    return df_T