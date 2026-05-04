import pandas as pd

CAMPANHAS_VALIDAS = ["7171",
                     "7301",
                     "WF"]

def filtrar_campanhas(df: pd.DataFrame) -> pd.DataFrame:
    
    df_filtrado = df[df["acao"].isin(CAMPANHAS_VALIDAS)]
    
    return df_filtrado