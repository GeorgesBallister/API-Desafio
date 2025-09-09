# Aqui contera todas as funções remetentes aos endpoints: DELETE

# * Bibliotecas e Modulos
import json
from flask import jsonify
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# * Exclui um dado pelo ID
## Endpoint que será utilizado: '/users/<user_id>'
def ApagarDadosPorID(DADOSBD, user_id):
    
    # 1: Ler o Banco e armazena
    registros_Do_DB = load_data(DADOSBD);

    # 2: Filtra todos os registros, deixando de fora apenas o registro que possuir o Id igual ao parametro 'user_id' passado no escopo do endpoint.
    registrosFiltrados = [registro for registro in registros_Do_DB # Ele percorre atravez de um loop cada registro o armazenando-o na nova lista
                          if registro.get("id") != user_id] # Aqui ele define que salvara apenas os registros que tem o valor da key 'id' diferente do valor do parametro 'user_id'

    # 3: Comparamos dois valores para verificar se aquele registro realmente existe:
    # valor 1: Comprimento da lista que tem apenas os valores filtrado
    # valor 2: Comprimento da lista original com todos os valores.
    # Se seus valores forem os mesmos, significa que não existia aquele id passado no parametro "user_id", ou seja a lista dos 'registrosFiltrados' não teria 1 valor a menos, visto que todos os id's são unicos e estariamos removendo aquelea resgistro que queriamos.
    if len(registrosFiltrados) == len(registros_Do_DB):
       # 3.1: Se os valores forem iguais ele retornara a mensagem de erro 404 (Não Encontrado) junto com o ID que foi passado
       return jsonify({
        "Erro" : f"Não foi possivel encontrar este usuario {user_id}, verifique sua solicitação"
    }), 404

    # 4: Caso o tamanho da lista de 'registrosFiltrados' tenha um valor diferente da lista original (nesse caso -1), ele pulara a estrutura condicinal acima.
    # Abrira o arquivo 'allData.jso' e salvara a lista filtrada subistituindo o JSON antigo
    with open(DADOSBD, "w") as f:
        json.dump(registrosFiltrados, f)

    # 5: Retornara uma mensagem 200 (OK), mostrando o sucesso na exclusão + o id que foi excluido. 
    return jsonify({"message": f"Usuário com id {user_id} deletado com sucesso"}), 200

