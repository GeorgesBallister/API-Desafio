# Aqui contera todas as funções remetentes aos endpoints: GET
from flask import request, jsonify
from utils.modules.ManipulacaoDeDados import load_data

# * Econtrar Dados Por Nome E Email
## Endpoint: '/users/find/'

def EcontrarDadosPorNomeEEmail(DADOSBD):
    
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