import pandas as pd
import os
from pathlib import Path

def salvar_arquivo(df):
    """Função para Salvar o Dataframe de negócios"""

    # Criando a pasta / Verificando existência
    Path("output").mkdir(parents=True, exist_ok=True)

    # Monta o caminho do arquivo

    caminho = Path("output") / "hubspot_deals.xlsx"

    df.to_excel(caminho, index=False)
    
    return caminho