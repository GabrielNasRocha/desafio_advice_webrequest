from src import WebRequests, escrever_json


def execute():
    print("Iniciando Automação de webscrapping")
    print("Criando e zerando o arquivo json")
    escrever_json({})
    fornecedores = {"Fornecedores": []}
    print("Chamando a função de coleta dos valores da WEB")
    web = WebRequests()
    print("Valores coletados")
    resultados = web.coletar_dados()
    for resultado in resultados:
        print(
            resultado["id"],
            resultado["nome"],
            resultado["cidade"],
            resultado["categoria"],
            resultado["situacao"]
        )
        fornecedor = {
                    "id": resultado["id"],
                    "nome": resultado["nome"],
                    "cidade": resultado["cidade"],
                    "categoria": resultado["categoria"],
                    "situacao": resultado["situacao"]
        }
        fornecedores["Fornecedores"].append(fornecedor)
    print("Valores formatados em json. Inserindo no arquivo")
    escrever_json(fornecedores)
    print("PROCESSO FINALIZADO")
if __name__ == "__main__":
    execute()
