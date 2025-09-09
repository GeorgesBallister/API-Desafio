# Aqui contera todas as funções remetentes aos endpoints: POST
from flask import request, jsonify

# Importando os modulos
from utils.modules.ManipulacaoDeDados import load_data, save_data
from utils.modules.GerarID import gerarID

def NovoRegistro(DADOSBD):
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

   # Definindo a estrutura da chave "page"
    dadosDoBody["page"] = dadosDoBody.get("page", {})

    page_size = dadosDoBody["page"].get("page_size")

    if not isinstance(page_size, int) or page_size < 10 or page_size > 50:
        dadosDoBody["page"]["page_size"] = 10
    else:
        dadosDoBody["page"]["page_size"] = page_size

    pageActual = dadosDoBody["page"].get("pageActual")

    if not isinstance(pageActual, int) or pageActual <= 0 or pageActual > dadosDoBody["page"]["page_size"]:
        dadosDoBody["page"]["pageActual"] = 1
    else:
        dadosDoBody["page"]["pageActual"] = pageActual


    # ! Gerando ID unico
    idNovo = gerarID(DADOSBD)
    dadosDoBody["id"] = idNovo

    # Salvando os dados no JSON
    save_data(dadosDoBody, DADOSBD)
    return jsonify({"message": "Usuário cadastrado com sucesso!", "usuario": dadosDoBody}), 201
