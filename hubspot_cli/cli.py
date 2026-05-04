from reporter import salvar_arquivo
from extractor import fazer_requisicao, PROPIEDADES
from transformer import filtrar_campanhas

if __name__ == "__main__":

    requisicao = fazer_requisicao("deals", PROPIEDADES)
    filtro = filtrar_campanhas(requisicao)
    arquivo = salvar_arquivo(filtro)



