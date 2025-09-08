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

# Carrega os dados:
registros_Do_DB = load_data(DADOSBD);


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
@app.route('/users/find/', methods=['GET'])
def QueryNameANDEmail():

    # Argumentos que serão mandados pelo get no corpo do JSON de Request
    nome = request.args.get("nome").strip().lower()
    email = request.args.get("email").strip().lower()


    for registro in registros_Do_DB:
        nome_registrado = str(registro.get("nome", "")).strip().lower()
        email_registrado = str(registro.get("email", "")).strip().lower()
        if nome_registrado == nome and email_registrado == email:
            return jsonify({
                "Usuario" : registro
            }), 200
        
        return jsonify({
            "Erro" : "Não foi possivel encontrar este usuario, verifique sua solicitação"
        }), 404
# Atualiza dado (Put)
#@app.route('/users/', methods=['PUT'])

# Deleta Dados (Delete)
#@app.route('/users/all', methods=['DELETE'])


# Rodar API
app.run(host='127.0.0.1', # IP
        port=5000, # Porta
        debug=True) # Debug