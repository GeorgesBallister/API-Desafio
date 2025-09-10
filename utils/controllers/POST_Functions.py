# Aqui contera todas as funções remetentes aos endpoints: POST

# * Bibliotecas e Modulos
from flask import request, jsonify
from utils.modules.ManipulacaoDeDados import load_data, save_data
from utils.modules.GerarID import gerarID
from datetime import datetime

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# * Registra um novo dado dentro do banco de dados
## Endpoint que será utilizado: '/users/'
def NovoRegistro(DADOSBD):
     # 1: Ler o Banco e armazenar
    registros_Do_DB = load_data(DADOSBD);

    # 2: Armazenar o escopo do body JSON do HTTP Request
    dadosDoBody = request.get_json() or {}
    
    # 3: Define os dados obrigatorios dentro do escopo do JSON
    listaDeDadosObrigatorios = ['name', 'email','role'];

    # 4: Verificação dos dados obrigatorios dentro do escopo do JSON

    if any( # 4.5: Aqui ele verificar se qualquer um dos dadps array que esse loop gerou tem pelomenos 1 item "TRUE", se ele tiver esse if é executado.
        
        dadoObrigatorio not in dadosDoBody  # 4.2: Depois ele vai verificar a cada loop que ele passar se esses campos NÃO estão dentro do escopo do JSON no body (Retornando True)

        or not dadosDoBody[dadoObrigatorio] # 4.3: Se o campo existir ele verificara se o campo esta sem qualquer tipo de valor (Tambem retornando "True")

        for dadoObrigatorio in listaDeDadosObrigatorios # 4.1: Percorre por toda a lista que contem todos os dados que serão obrigatorios, armazenando qual informação ele vai verificar naquele loop.

        # 4.4: Por fim ele gera um array de boolean para cada item da "listaDeDadosObrigatorios"
        # True = Campo não exite
        # False = Campo existe
        ):
        
        # 4.6: Retona o erro caso algum campo obrigatorio não tenha sido passado no body
        return jsonify({"error": "Dados inválidos: Todos os campos são obrigatórios", "campos_obrigatorios": listaDeDadosObrigatorios}), 400
    
        # 4-Recaptulado:
        """
        1- Ele vai pegar os dois campos que foi passado como obrigatorio 'nome' e 'email', que estão armazenados dentro da variavel "listaDeDadosObrigatorios".

        2- Depois ele vai pegar esses campos e passar uma checagem de ler 1 dado obrigatorio por vez e verificar se ele esta NÃO esta presente no escopo do body do HTTP Request.
        
        3- Se o respectivo campo NÃO EXISTIR ele vai passar nesse teste e vai retornar como TRUE, se o campo EXISTIR ele vai falhar no teste e rentornar como FALSE.

            3.1 - Gerando assim por exemplo se o campo nome existir dentro do body mais o email não ele ficaria assim [False, True]

        4. Se no final do teste de todos os campos obrigatorios existir pelomenos um True("Aquele dado não esta no body do HTTP Request") ele retornara a mensagem de erro 400.

        4.1 Se todos os campos forem falsos ele vai passar pular este erro. 
        """


    
    # 5: Verifica se já existe aquele email dentro da base de dados
    # 5.1: Um loop é utilizado para percorrer cada um dos itens dentro da lista de registros_Do_DB 
    for registro in registros_Do_DB:
        
        # 5.2: Verifica da seguinte forma:
        # Ele vai comparar dois valores
        # Valor 1: O dado da key "email", do registro do banco de dados daquele momento do loop, formatado com todas as letras minusculas
        # Valor 2: O dado da key "email", do body do HTTP Request, formatado com todas as letras minusculas.
        if registro.get("email", "").strip().lower() == dadosDoBody["email"].strip().lower():
            # 5.3: Se pelomenos 1 comparação retortnar como True, ele ira executar esta mensagem de erro 409 (Conflito), senão ele so vai pular esta linha
            return jsonify({"error": "Este email já esta cadastrado em nosso sistema, por favor tente outro ."}), 409

    
   # 6: Definindo a estrutura e armazenando os valores da key "page"
    dadosDoBody["page"] = dadosDoBody.get("page", {})

    # 7: Armazenando a informação de "page_size" do escopo do body em uma variavel
    page_size = dadosDoBody["page"].get("page_size")

    # 8: Verificando se as informações de page_size estão corretas
    # 8.1: Aqui vai ser verificado o seguinte (em ordem):
    # O campo page_size existe, se não, existir ele retorna True
    # Ou se o campo page_size é menor que 10 ou maior que 50 se sim, ele retorna True
    if not isinstance(page_size, int) or page_size < 10 or page_size > 50:
        # 8.1.1: Se todas pelomenos um dos retornos derem True, ele define que o valor base da key "page_size", dentro da key "page", como 10
        dadosDoBody["page"]["page_size"] = 10
    # 8.1.2: Caso todos os testes retornem como False, significa que o campo já existe no body do HTTP Request e ele atende a os requisitos solicitados
    # Isso significa que ele armazenou algum valor dentro da variavel 'page_size' (#7).
    else:
        # Ele vai pegar esta informação armazenada na variavel 'page_size' e vai agragar a o valor da key 'page_size' no escopo do body
        dadosDoBody["page"]["page_size"] = page_size

    # 9: Armazenando a informação de "pageActual" do escopo do body em uma variavel
    pageActual = dadosDoBody["page"].get("pageActual")

    # 10: Verificando se as informações de pageActual estão corretas
    # 10.1: Aqui vai ser verificado o seguinte (em ordem):
    # O campo pageActual existe, se não, existir ele retorna True
    # Ou se o campo pageActual é menor ou igual a 0, ou maior que o tamnho do valor da key 'page_size' no escopo do body se sim, ele retorna True
    if not isinstance(pageActual, int) or pageActual <= 0 or pageActual > dadosDoBody["page"]["page_size"]:
        
        # 10.1.1: Se todas pelomenos um dos retornos derem True, ele define que o valor base da key "pageActual", dentro da key "page", como 1
        dadosDoBody["page"]["pageActual"] = 1
    
    # 10.1.2: Caso todos os testes retornem como False, significa que o campo já existe no body do HTTP Request e ele atende a os requisitos solicitados
    else:
        # Ele vai pegar esta informação armazenada na variavel 'pageActual' e vai agragar a o valor da key 'pageActual' no escopo do body
        dadosDoBody["page"]["pageActual"] = pageActual


    # ! Gerando ID unico
    # 11: Aqui ele vai gerar um novo ID, utilizando da função presente no modulo utils.modules.GerarID 
    idNovo = gerarID(DADOSBD)

    # 12: Vai agregar o novo ID a key 'id' dentro no escopo do body
    dadosDoBody["id"] = idNovo

    # 13: Gerar o valor do campo Is_active
    # 13.1: Primeiramente devemos procurar se o valor existe armazenamos oque esta no campo
    is_activeValor = dadosDoBody.get("is_active")

    # 13.2: Valida-se se o campo não tem algum valor, se ele não tiver, por padrão vamos colocar como TRUE.
    if not isinstance(is_activeValor, bool):
        dadosDoBody["is_active"] = True
    
    # 13.2.1 Caso o campo já vinher com algum valor do body, somente colocamos ele no mesmo canto
    else:
        dadosDoBody["is_active"] = is_activeValor


    # 14: Gera uma variavel com o registro do tempo naquele momento
    timeNow = datetime.now()
    # 14.1: Formata o texto para ficar igual a referencia do MOCK-USERS
    timeNowFormatado = timeNow.strftime("%Y-%m-%dT%H:%M:%SZ")
    dadosDoBody['created_at'] = timeNowFormatado

    # 15: Aqui ele vai salvar os dados no JSON usando a função do modolulo utils.modules.ManipulacaoDeDados
    save_data(dadosDoBody, DADOSBD)

    # 16: Se tudo ocorrer certo, a função vai retornar uma mensagem de sucesso 201 (criado) e junto a ela dentro do body do HTTP Response vira o novo dado que foi registrado.
    return jsonify({"message": "Usuário cadastrado com sucesso!", "usuario": dadosDoBody}), 201

