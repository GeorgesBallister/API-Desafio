# Aqui contera todas as funções remetentes aos endpoints: GET

# * Bibliotecas e Modulos
from flask import request, jsonify
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# This section of code defines a function called `EcontrarDadosPorNomeEEmail` that
# is responsible for finding data based on a given name and email. It is designed
# to be used as an endpoint in a Flask application with the route '/users/find/'.

# * Econtrar Dados Por Nome E Email
## Endpoint que será utilizado: '/users/find/'

def EcontrarDadosPorNomeEEmail(DADOSBD):
    
    # 1: Ler o Banco e armazena
    registros_Do_DB = load_data(DADOSBD);

    # 2: Define os argumentos obrigatorios que serão mandados pelo get no corpo do Request como parametros no endpoint
    # 2.1: transforma ambos os dois campos (nome e email) em 2 variaveis com seu respectivo nome, porem com os dados normalizados em letras minusculas para facilitar a verificação no banco de dados.
    nome = request.args.get("nome").strip().lower()
    email = request.args.get("email").strip().lower()

    # 3: Roda um loop passando por todos os registros do banco de dados.
    for registro in registros_Do_DB:
        # 3.1: Cada loop que este laço de repetição da vai armazenar 2 valores por vez:
            # O valor da key 'nome' do registro daquele momento e o valor da key 'email'
        # Obtendo seus valores atravez da função 'get' que está presente no elemento individual da lista
        # Normalizando seus valores em letras minusculas
        nome_registrado = str(registro.get("nome", "")).strip().lower()
        email_registrado = str(registro.get("email", "")).strip().lower()
        
        # 3.2: Aqui cada loop do laço de repetição vai verificar os valores das key's salvas com os valores dos argumentos passados.
        # Verificando se ambos os dois valores retornam como True (valores dos argumentos = valor das chaves no momento do loop)
        if nome_registrado == nome and email_registrado == email:
            # 3.4: Se ambos os valores True, esta função retonrara uma mensagem de sucesso 200 (OK), junto com os dados do usuario encontrado.
            return jsonify({
                "Usuario" : registro
            }), 200
    # 3.5: Caso o contrario, se não passar na verificação ele retornara um 404 (Não Encontrado), junto com um aleta no escopo do HTTP Response
    return jsonify({
        "Erro" : "Não foi possivel encontrar este usuario, verifique sua solicitação"
    }), 404