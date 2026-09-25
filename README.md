# Desafio Advice WebRequest 💡

Este projeto em Python consome dados de fornecedores de uma API da empresa ADVICE (usando requisições web) e faz o gerenciamento/salvamento desses dados em arquivos JSON locais.

---

## 📁 Estrutura do Projeto

```text
desafio_advice_webrequest/
├── files/
│   ├── fornecedores.json
├── src/
│   ├── __init__.py
│   ├── webRequests.py      # Módulo responsável por realizar requisições HTTP para a API de conselhos
│   └── json_manager.py     # Módulo responsável pelo tratamento e salvamento dos dados em JSON
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## 🚀 Funcionalidades

- **Consumo de API Externa:** Busca conselhos aleatórios ou específicos via HTTP (`webRequests.py`).
- **Gerenciamento de Arquivos JSON:** Armazena, lê e manipula as respostas no formato JSON localmente (`json_manager.py`).
- **Execução Centralizada:** Fluxo simples orquestrado pelo arquivo principal `main.py`.

---

## 🛠️ Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

---

## 🔧 Configuração e Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/desafio_advice_webrequest.git
   cd desafio_advice_webrequest
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🟢 Como Executar

Após instalar as dependências, execute a aplicação rodando o arquivo `main.py`:

```bash
python main.py
```

---

## 🧰 Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal do projeto.
- **[Requests](https://requests.readthedocs.io/):** Biblioteca para requisições HTTP.
- **JSON:** Formato padrão para manipulação de dados armazenados.