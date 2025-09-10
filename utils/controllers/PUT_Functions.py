# Aqui contera todas as funções remetentes aos endpoints: PUT

# * Bibliotecas e Modulos
from flask import request, jsonify
import json
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# * Atualiza um dado pelo ID
## Endpoint que será utilizado: '/users/update/<user_id>'
def AtualizarRegistroPorID(DADOSBD, user_id):
    
     # 1: Ler o Banco e armazenar
    registros_Do_DB = load_data(DADOSBD);

    # 2: Armazenar o escopo do body JSON do HTTP Request
    dadosDoBody = request.get_json() or {}

    # 3: Se o body estiver vazio retornar mensagem de erro 400(Bad Request)
    if not dadosDoBody:
        return jsonify({
            "error": "Nenhum dado enviado para atualização"
            }), 400
    

    # 4: Verificando se já existe aquele email percorrento todos os registros armazenados como lista
    for registro in registros_Do_DB:
        # 4.1: Cada loop que este laço de repetição da vai armazenar o valor da key 'email' do registro daquele momento
        # Obtendo o valor da key 'email' atravez da função 'get' que está presente no elemento individual 'registro' da lista do Banco de dados
        # Normalizando seus valores em letras minusculas
        if registro.get("email", "").strip().lower() == dadosDoBody["email"].strip().lower():
            # Se esta operação condicional retornar como True, significa que dentro do sistema
            return jsonify({"error": "Este email já esta cadastrado em nosso sistema, por favor tente outro ."}), 409
    
    # * Verificando se usuario existe pelo ID
    # 5: Cria esta variavel como false para depois preenchela caso o usuario sejá encontrado pelo seu ID's, servindo posteriormente de variavel de controle
    usuario_encontrado = False

    # 6: Cria a um laço de repetição com dois elementos individuais:
    # indiceDoRegistro = a posição do usuario na lista
    # registro = os dados do usuario
    # Este laço de repeticção vai se basear em fornecer essas 2 informações por vez 
    for indiceDoRegistro, registro in enumerate(registros_Do_DB):
        # 6.1: Se o "user_id" fornecido como argumento no url do endpoint tiver o mesmo valor id da key "id" dentro dos registros ele executara.
        if str(registro.get("id")) == str(user_id):

            # 6.1.1: Aqui vai fazer a atualização dos novos dados
            # Ele vai percorrer o conteudo do body do HTTP Request, atraves de um laço de repetição com dois elementos individuais:
            # chave = Vai representar a key daquele momento
            # valor = Vai representar o valor que sera colocado naquela key 
            for chave, valor in dadosDoBody.items():
                registro[chave] = valor
            
            # 6.1.2: Assim que todo o body for percorrido ele pegara qual a posição que aquele registro estava dentro da lista, e subistituira seus valores pelos novos que estarão dentro do body do HTTP Request
            registros_Do_DB[indiceDoRegistro] = registro
            # 6.1.3: Ele trocara o valor do usuario_encontrado para True e quebrara o loop não permitindo que a validação de usuario não encontrado seja executado.
            usuario_encontrado = True
            break
    # 6.2: Se nenhum 'user_id', tiver o mesmo valor de id do parametro da requisição 'id', o estado de 'usuario_encontrado' nunca mudara, então consequentemente esta parte do codigo executara.
    # Retornando assim uma mensagem 404 (Não encontrado)
    if not usuario_encontrado:
       return jsonify({
        "Erro" : f"Não foi possivel encontrar este usuario {user_id}, verifique sua solicitação"
    }), 404


    # 7: Salva o registro sobrescrendo o JSON antico com o JSON modificado
    with open(DADOSBD, "w") as f:
        json.dump(registros_Do_DB, f)
    # 8: Retorna uma mensagem 200 (OK), alterando o dado, e exibindo as alterações no body do HTTP Response
    return jsonify({
        "message": "Usuário atualizado com sucesso",
        "usuario": registro
    }), 200

