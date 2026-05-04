import pandas as pd
from transformer import filtrar_campanhas


arquivo_demo = {
    'id': [1234, 45678, 91011, 121314, 151617, 182920, 212223, 242526, 272829],
    'acao': ["D", 
             "E",
             "M",
             "O",
             "WCFO",
             "Demo",
             "Teste",
             "Não passar",
             "Não passar 2"
             ]
}

df = pd.DataFrame(arquivo_demo)

def test_filtrar_campanhas():
    
    resultado = filtrar_campanhas(df)
    
    assert len(resultado) == 5
