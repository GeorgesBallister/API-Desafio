# Aqui contera todas as funções remetentes aos endpoints: DELETE

# * Bibliotecas e Modulos
import json
from flask import jsonify
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".


def ApagarDadosPorID(DADOSBD, user_id):
     # Lendo o Banco
    registros_Do_DB = load_data(DADOSBD);

    registrosFiltrados = [registro for registro in registros_Do_DB if registro.get("id") != user_id]

    if len(registrosFiltrados) == len(registros_Do_DB):
       return jsonify({
        "Erro" : f"Não foi possivel encontrar este usuario {user_id}, verifique sua solicitação"
    }), 404

    # Salva a lista filtrada de volta no JSON
    with open(DADOSBD, "w") as f:
        json.dump(registrosFiltrados, f)

    return jsonify({"message": f"Usuário com id {user_id} deletado com sucesso"}), 200

