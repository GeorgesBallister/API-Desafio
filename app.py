# Bibliotecas
from flask import Flask, request, jsonify
import json
import os

# Importando os Utils
from utils.ManipulacaoDeDados import load_data, save_data, load_moc
from utils.GerarID import gerarID

# ! Instância Flask e Nome da API
app = Flask("API-Valcann") 

# "Banco"
DADOSBD = "Data/allData.json"

# Carrega os dados:



# ! Endpoints

# Mock
@app.route('/moc', methods=['POST'])
def Mock():
    return load_moc(DADOSBD)

# Atualiza dado (Put)
# @app.route('/users/register', methods=['POST'])
# def registrar_usuarios():
    

# Lista todos (Get)
@app.route('/users/all', methods=['GET'])
def ReturnALLData():
    return load_data(DADOSBD)

# Encontra pelas "Primary Key" "Nome e Email" (Get)
@app.route('/users/find/', methods=['GET'])
def QueryNameANDEmail():

    # Lendo o Banco
    registros_Do_DB = load_data(DADOSBD)

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

# Registro no Banco (Post)
@app.route('/users/', methods=['POST'])
def Register_User():
    # Lendo o Banco
    registros_Do_DB = load_data(DADOSBD);

    # Aqui vai ser armazenado oque o usuario colocar no body do HTTP Request
    dadosDoBody = request.get_json() or {}
    
    # Dados que toda requisição vai ser obrigada a ter
    dadosObrigatorios = ['nome', 'email'];

    # Validação para saber se os dados obrigatoris foram colocados
    if any(dadoObrig not in dadosDoBody or not dadosDoBody[dadoObrig] for dadoObrig in dadosObrigatorios ):
        return jsonify({"error": "Dados inválidos: Todos os campos são obrigatórios", "campos_obrigatorios": dadosObrigatorios}), 400
    
    # Verificando se já existe aquele email
    for registro in registros_Do_DB:
        if registro.get("email", "").strip().lower() == dadosDoBody["email"].strip().lower():

            return jsonify({"error": "Este email já esta cadastrado em nosso sistema, por favor tente outro ."}), 409

    # ! Gerando ID unico
    idNovo = gerarID(DADOSBD)
    dadosDoBody["id"] = idNovo

    # Salvando os dados no JSON
    save_data(dadosDoBody, DADOSBD)
    return jsonify({"message": "Usuário cadastrado com sucesso!", "usuario": dadosDoBody}), 201




# Deleta Dados (Delete)
#@app.route('/users/all', methods=['DELETE'])


# Rodar API
app.run(host='127.0.0.1', # IP
        port=5000, # Porta
        debug=True) # Debug