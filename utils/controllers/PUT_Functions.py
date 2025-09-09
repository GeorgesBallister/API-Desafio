# Aqui contera todas as funções remetentes aos endpoints: PUT

# * Bibliotecas e Modulos
from flask import request, jsonify
import json
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# * 
def AtualizarRegistroPorID(DADOSBD, user_id):
    # Lendo o Banco
    registros_Do_DB = load_data(DADOSBD);

    # Aqui vai ser armazenado oque o usuario colocar no body do HTTP Request
    dadosDoBody = request.get_json() or {}

    # se o body estiver vazio
    if not dadosDoBody:
        return jsonify({
            "error": "Nenhum dado enviado para atualização"
            }), 400
    
    usuario_encontrado = False

    # Verificando se já existe aquele email
    for registro in registros_Do_DB:
        if registro.get("email", "").strip().lower() == dadosDoBody["email"].strip().lower():

            return jsonify({"error": "Este email já esta cadastrado em nosso sistema, por favor tente outro ."}), 409


    for indiceDoRegistro, registro in enumerate(registros_Do_DB):
        if registro.get("id") == user_id:

            # Aqui vai fazer a atualização
            for chave, valor in dadosDoBody.items():
                registro[chave] = valor
            
            registros_Do_DB[indiceDoRegistro] = registro
            usuario_encontrado = True
            break
    if not usuario_encontrado:
       return jsonify({
        "Erro" : f"Não foi possivel encontrar este usuario {user_id}, verifique sua solicitação"
    }), 404


    # Salva o registro sobrescrendo o JSON
    with open(DADOSBD, "w") as f:
        json.dump(registros_Do_DB, f)

    return jsonify({
        "message": "Usuário atualizado com sucesso",
        "usuario": registro
    }), 200

