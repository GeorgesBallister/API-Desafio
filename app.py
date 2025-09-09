"""
    Desenvolvedor : Georges Ballister de Oliveira
    Tempo de Desenvolvimento: 07/09/2025 23:00h - 08/09/2025 21:45
    Objetivo: Desenvolvi este sistema com o intuito de realizar a avaliação Técnica do Processo Seletivo: Desenvolvedor(a) Back-end Júnior para a empresa VALCANN, escolhi implementar uma ideia que eu julguei ser o mais intuitivo possivel e direto a fim de facilitar o trabalho de quem for avaliar este software, acabei por optar em desenvolver esta API para que se possa interagir com um "pseudo banco de dados", que na verdade é um arquivo json, que esta no diretorio "/Data/allData.json".
    
    Alem disto "Dockerizei" a aplicação para que se transforme em algo mais facil de implementar em um mini projeto um pouco mais fidedigno com a area de atuação da VALCANN, ou seja, podendo rodar em "nuvem" optimizando o uso dos recursos.
    Link do Docker-HUB: 

    Aviso:
    Para sua leitura ficar mais facil, meus comentarios no codigo utilizaram os incrementos que a extensão "Better Comments" by "Aaron Bond", este apelo visual pode ajudar na sua leitura! Desde já agradeço por esta oportunidade.
"""


# Bibliotecas que vou usar para fazer a construção da API (FLASK)
from flask import Flask


# ! ====================== MODULES ======================
# * Bem, aqui resolvi separa todos as "funções (def)" que os endpoints executam em modulos todos organizados dentro da pasta utils, podendo ter assim um controle muito mais versatil de como cada função vai interagir com o meu ambiente da API, isolando todos os problemas em seus respectivos lugares e adotando alguns dos conceitos abordados pelo livro "Codigo Limpo", só que aplicado ao contexto do meu ambiente e tecnologia.

# * Dito isto, todas as novas funções que forem criadas devem seguir esta "regra de negocio" para que se mantenha o ambiente organizado e facilite a manutenibilidade.

# Importando os modulos Para o MOC ('/moc', methods=['POST']) e O metodo de "getAll" ('/users/all', methods=['GET'])
from utils.modules.ManipulacaoDeDados import load_data, load_moc

# Modulo para funções de POST
from utils.controllers.POST_Functions import NovoRegistro

# Modulo para funções de GET
from utils.controllers.GET_Functions import EcontrarDadosPorNomeEEmail

# Modulo para funções de PUT
from utils.controllers.PUT_Functions import AtualizarRegistroPorID

# Modulo para funções de DELETE
from utils.controllers.DELETE_Functions import ApagarDadosPorID

# ! Instância Flask e Nome da API
app = Flask("API-Valcann") 

# "Banco" este pseudo banco de dados NOSQL vai ser por completo concentrado dentro de um arquivo JSON, utilizando de sua estrutura versatio, eu consegui desenvolver todos os conceitos do CRUD dento da arquitetura de uma REST API, com todos os HTTP METHODS interagindo com este arquivo atraves dos endpoints
DADOSBD = "Data/allData.json"

# ! ====================== Endpoints ======================

## === HTTP POST's ===

# * Mock (Inserir os dados Ficticios)
@app.route('/moc', methods=['POST'])
def Mock():
    return load_moc(DADOSBD)

# * Registro no Banco (Post)
@app.route('/users/', methods=['POST'])
def Register_User():
   return NovoRegistro(DADOSBD)


## === HTTP GET's ===

# * Lista todos (Get)
@app.route('/users/all', methods=['GET'])
def ReturnALLData():
    return load_data(DADOSBD)

# * Encontra pelas "Primary Key" "Nome e Email" (Get)
@app.route('/users/find/', methods=['GET'])
def QueryNameANDEmail():
    return EcontrarDadosPorNomeEEmail(DADOSBD);


## === HTTP PUT's ===

# * Atualiza dado (Put)
@app.route('/users/update/<user_id>', methods=['PUT'])
def atualizar_Registro(user_id):
    return AtualizarRegistroPorID(DADOSBD, user_id)


## === HTTP DELETE's ===

# * Deleta Dados (Delete)
@app.route('/users/<user_id>', methods=['DELETE'])
def Apagar_Usuario(user_id):
   return ApagarDadosPorID(DADOSBD, user_id)


# ! Rodar API
app.run(host='0.0.0.0', # IP para poder ficar exposto no Docker
        port=5000, # Porta
        debug=True) # Debug