import requests


class WebRequests:
    def __init__(self):
        self.tokenSessao = "706c942608134fa094bc5a98142bd198"
        self.baseURL = "https://interview.advicek8s.dpdns.org/api/sessions/junior-scrape/site"

    def coletar_dados(self):
        print("WebRequests: Criando a sessão para o requests")
        session = requests.Session()
        session.cookies.set(
            "iv_site",
            self.tokenSessao,
            domain="interview.advicek8s.dpdns.org"
        )
        print("WebRequests: Chamando a API de coleta de token")
        resposta = session.get(
            f"{self.baseURL}/api/token"
        )
        if resposta.status_code != 200:
            print("Erro:", resposta.status_code)
            return
        token_api = resposta.json()["token"]
        print("WebRequests: Buscando a lista de fornecedores")
        resposta = session.get(
            f"{self.baseURL}/api/listings",
            params={"token": token_api}
        )
        if resposta.status_code != 200:
            print("Erro:", resposta.status_code)
            return
        print("WebRequests: Fornecedores coletados com sucesso")
        return resposta.json()
