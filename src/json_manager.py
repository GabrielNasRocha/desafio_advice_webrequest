import json

def escrever_json(dados):
    path = "files/fornecedores.json"
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )