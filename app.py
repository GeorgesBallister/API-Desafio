"""
    Desenvolvedor : Georges Ballister de Oliveira
    Tempo de Desenvolvimento: 07/09/2025 23:00h - 08/09/2025 21:45
    Objetivo: Desenvolvi este sistema com o intuito de realizar a avaliação Técnica do Processo Seletivo: Desenvolvedor(a) Back-end Júnior para a empresa VALCANN, escolhi implementar uma ideia que eu julguei ser o mais intuitivo possivel e direto a fim de facilitar o trabalho de quem for avaliar este software, acabei por optar em desenvolver esta API para que se possa interagir com um "pseudo banco de dados", que na verdade é um arquivo json, que esta no diretorio "/Data/allData.json".
    Alem disto "Dockerizei" a aplicação para que se transforme em algo mais facil de implementar em um mini projeto um pouco mais fidedigno com a area de atuação da VALCANN, ou seja, podendo rodar em "nuvem" optimizando o uso dos recursos.
"""


# Biblioteca que vou usar para fazer a construção da API (FLASK)
from flask import Flask


# Importando os modulos de
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

# "Banco"
DADOSBD = "Data/allData.json"

# ! Endpoints

# * Mock (Inserir os dados Ficticios)
@app.route('/moc', methods=['POST'])
def Mock():
    return load_moc(DADOSBD)

# * Lista todos (Get)
@app.route('/users/all', methods=['GET'])
def ReturnALLData():
    return load_data(DADOSBD)

# * Encontra pelas "Primary Key" "Nome e Email" (Get)
@app.route('/users/find/', methods=['GET'])
def QueryNameANDEmail():
    return EcontrarDadosPorNomeEEmail(DADOSBD);

# * Registro no Banco (Post)
@app.route('/users/', methods=['POST'])
def Register_User():
   return NovoRegistro(DADOSBD)

# * Atualiza dado (Put)
@app.route('/users/update/<user_id>', methods=['PUT'])
def atualizar_Registro(user_id):
    return AtualizarRegistroPorID(DADOSBD, user_id)

# * Deleta Dados (Delete)
@app.route('/users/<user_id>', methods=['DELETE'])
def Apagar_Usuario(user_id):
   return ApagarDadosPorID(DADOSBD, user_id)


# Rodar API
app.run(host='127.0.0.1', # IP
        port=5000, # Porta
        debug=True) # Debug