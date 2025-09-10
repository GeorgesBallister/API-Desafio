# 📄 API REST + CORS (Tudo Local) - Desafio Valcann

<div style="text-align: center;">
  <img src="./Documentacao/valcann-logo.png" alt="Logo" style="display: inline-block;">
</div>


## 📌 Descrição do Projeto

Este projeto consiste em uma **API RESTful** desenvolvida em **Python com Flask**, implementando todas as operações do **CRUD** (Create, Read, Update, Delete) utilizando um **pseudo banco de dados em JSON**.

O objetivo foi criar um ambiente simples e funcional para avaliação técnica da posição de **Desenvolvedor(a) Back-end Júnior** na **VALCANN**. Além disso, o projeto serve como referência para aprender boas práticas de **REST API**, **Docker** e **testes automatizados**.

---

## ⚙️ Tecnologias Utilizadas

<div style="display: flex; justify-content: center; gap: 50px;">
<img  align="center" alt="PI-PYTHON" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
<img  align="center" alt="PI-FLASK" height="60" width="60"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />
<img  align="center" alt="PI-DOCKER" height="60" width="60"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" />
<img  align="center" alt="PI-POSTMAN" height="50" width="50"   src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postman/postman-original.svg" />
<img align="center" alt="PI-JSON" height="50" width="50"   src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" />  
</div>

---

## 🚀 Principais Funcionalidades

- 👤 Cadastro de usuários (`POST /users/`)
- 📋 Listagem de usuários (`GET /users/all`)
- 🔎 Busca de usuários por nome e e-mail (`GET /users/find/`)
- ✏️ Atualização de usuários por ID (`PUT /users/update/<user_id>`)
- ❌ Exclusão de usuários por ID (`DELETE /users/<user_id>`)
- 🧪 Inserção de dados fictícios (Mock-Users) (`POST /mocValcann`)

O projeto também está **dockerizado** para facilitar a execução em ambientes isolados.

---

# 📂 Estrutura do Projeto


``` BASH
API-Valcann/
|   .dockerignore                 # Arquivos ignorados no contexto Docker
|   app.py                        # Arquivo principal da API (ponto de entrada Flask)
|   Dockerfile                    # Configuração para build da imagem Docker
|   README.md                     # Documentação do projeto
|   requirements.txt              # Dependências do Python
|   tests.py                      # Script de testes automatizados
|
+---Data
|       allData.json              # "Banco de dados" principal (pseudo NoSQL)
|       mock-users.json           # Dados fictícios para popular o sistema (MOC)
|
+---Documentacao
|       valcann-logo.png          # Logo para o README.md
|
\---utils
    |   __init__.py               # Identificação do pacote Python
    |
    +---controllers
    |   |   DELETE_Functions.py   # Funções para DELETE
    |   |   GET_Functions.py      # Funções para GET
    |   |   POST_Functions.py     # Funções para POST
    |   |   PUT_Functions.py      # Funções para PUT
    |   |   __init__.py           # Inicializador do subpacote
    |   |
    |   \---__pycache__           # Cache gerado pelo Python (.pyc)
    |
    +---modules
    |   |   GerarID.py            # Função utilitária para gerar IDs únicos
    |   |   ManipulacaoDeDados.py # Funções para manipulação do JSON (load, save, etc.)
    |   |   __init__.py
    |   |
    |   \---__pycache__           # Cache gerado pelo Python (.pyc)
    |
    \---__pycache__               # Cache do pacote utils
```


---

## 🔧 Pré-requisitos

- 🐍 **Python 3.9+**
- 📦 **pip** (gerenciador de pacotes Python)
- 🐳 **Docker** (opcional, para execução em container)
- 📮 **Postman** ou outro cliente HTTP para testes manuais

---

## 📦 Dependências

| Nome           | Versão | Descrição                                                                                                     |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| **Flask**      | 3.1.2  | Responsável por implementar APIs em Python, oferecendo suporte a **Requests HTTP** e **JSONIFY**              |
| **Flask-Cors** | 6.0.1  | Responsável por habilitar **Cross-Origin Resource Sharing (CORS)** para chamadas de diferentes origens         |

---

# ⚡ Instalando o Projeto

> 🔹 **Passo 1:** Clone o repositório e instale as dependências:

```bash
git clone <URL_DO_REPOSITORIO>
cd API-Valcann
pip install -r requirements.txt
````

> 🔹 **Passo 2:** Inicialize a aplicação:

```bash
python app.py
```

* A API será iniciada no **host 0.0.0.0** e na **porta 5000**.

---

## 🌐 Endpoints Disponíveis

| Método | Endpoint                  | Descrição                            |
| ------ | ------------------------- | ------------------------------------ |
| POST   | /users/                   | Cadastrar usuário                    |
| GET    | /users/all                | Listar todos os usuários             |
| GET    | /users/find/              | Buscar usuário por nome/e-mail       |
| PUT    | /users/update/\<user\_id> | Atualizar usuário                    |
| DELETE | /users/\<user\_id>        | Deletar usuário                      |
| POST   | /mocValcann               | Inserir dados fictícios (mock-users) |

---

## 🐳 Executando com Docker

> 🔹 **1. Construir a imagem:**

```bash
docker build -t api-valcann:v1 .
```

> 🔹 **2. Rodar o container:**

```bash
docker run -d -p 5000:5000 api-valcann:v1
```

* Agora a API estará acessível em `http://127.0.0.1:5000`.

---

## ✅ Testes Automatizados

O projeto possui um script `tests.py` que valida todos os endpoints automaticamente.

1. Certifique-se de que a API está rodando (localmente ou via Docker).
2. Execute em um terminal:

```bash
python tests.py
```

🔍 O script valida:

* Mock de dados (mock-users.json) — **Disponibilizado pela Valcann**
* Inserção de usuários (POST) — **5 cenários diferentes**
* Busca de usuários (GET) — **2 cenários diferentes**
* Atualização de usuários (PUT) — **2 cenários diferentes**
* Exclusão de usuários (DELETE) — **2 cenários diferentes**

➡️ Os resultados serão exibidos no terminal com status ✅ ou 🚫 para cada teste.

---

## 📌 Observações

* O **CORS** está habilitado para permitir chamadas de qualquer origem nos endpoints `/users/*`.
* O banco de dados é **pseudo**: os dados estão em `Data/allData.json` e podem ser sobrescritos durante testes e operações CRUD.
* Para **adicionar novos endpoints**, siga o padrão de organização por módulos dentro de `utils/controllers` e registre a rota no `app.py`.
* Todo o código está documentado com comentários explicativos para auxiliar no entendimento.

---

## 👨‍💻 Autor

**Georges Ballister de Oliveira**

* Desenvolvedor Full-Stack
* Criador desta API para a avaliação técnica da **VALCANN**
* 📧 Contato: [georgesballister.profissional@gmail.com](mailto:georgesballister.profissional@gmail.com)

<div style="display: flex; justify-content: center; gap: 50px;">
    <a href="https://github.com/GeorgesBallister"> 
        <img alt="PI-Github" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg"/> 
    </a>
    <a href="https://www.linkedin.com/in/georges-ballister-de-oliveira/"> 
        <img alt="PI-LINKEDIN" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg"/>
    </a>
</div>


