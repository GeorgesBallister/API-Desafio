# Bibliotecas
from flask import Flask, request, jsonify
import json
import os

# Importando os Utils
from utils.ManipulacaoDeDados import load_data, save_data, load_moc


# ! Instância Flask e Nome da API
app = Flask("API-Valcann") 

# "Banco"
DADOSBD = "Data/allData.json"

# Carregar dados assim que tudo inicializar:
usuarios = load_data(DADOSBD);


# ! Endpoints

# Mock
@app.route('/moc', methods=['POST'])
def Mock():
    return load_moc(DADOSBD)

# Registro no Banco (Post)
# @app.route('/users/register', methods=['POST'])
# def registrar_usuarios():
    

# Lista todos (Get)
@app.route('/users/all', methods=['GET'])
def RetornaTudo():
    return load_data(DADOSBD)

# Encontra pelas "Primary Key" "Nome e Email" (Get)
@app.route('/users/find', methods=['GET'])
def QueryNameANDEmail(){
    
}

# Atualiza dado (Put)
#@app.route('/users/', methods=['PUT'])

# Deleta Dados (Delete)
#@app.route('/users/all', methods=['DELETE'])


# Rodar API
app.run(host='127.0.0.1', # IP
        port=5000, # Porta
        debug=True) # Debug