# Bibliotecas
from flask import jsonify
import os
import json


# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".

# * Carrega os dados do arquivo JSON "allData.json"
def load_data(dadosDB):
    # 1: Verificar se o arquivo realmente existe
    if os.path.exists(dadosDB):
        # 2: Abrir o arquivo no modo de leitura
        with open(dadosDB, "r") as f:
            # 3: Criar um objeto json chamado de "dados"
            try:
                dados = json.load(f)
            # 3.1: Tratamento de erro 
            except json.JSONDecodeError:
                return []  # Arquivo vazio ou inválido → retorna lista vazia
        # 4: Padronização dos dados de saida para garantir que ele retorne uma lista de dados com cada registro no arquivo "allData.json"
        if isinstance(dados, dict):
            return [dados]
        elif isinstance(dados, list):
            return dados
        else:
            return []
    # Se o arquivo não existir ele só retornara um arquivo vazio
    else:
        return []  # Se não existir, retorna lista vazia


# * Esta vai ser a função utilizada para Salvar os dados novos no sistema o adcionando como um proximo dado registrado dentro do "allData.json"
# Esta função vai operar com 2 parametos:

# data = O dado Novo que vai entrar, ele tem que esta já formatado como uma dicionario de apenas uma dimenção , com seu escopo sem os colchetes "[" ou "]", ele deve esta sendo armazenado apenas com sua estrutura em dicionario encorpada com o uso das chaves "{" ou "}".
# dadosDB
def save_data(data, dadosDB):
    # 1: Carrega a verção atual do banco de dados e armazenalos na variavel "todosOsRegistros"
    todosOsRegistros = load_data(dadosDB)

    # 2: verifica se ele não é uma instancia de lista
    if not isinstance(todosOsRegistros, list):
        todosOsRegistros = []

    # 3: Adciona o novo dado que vai entrar no BD a os dados antigos
    todosOsRegistros.append(data)

    # 4: Abre o arquivo "allData.js" e sobrescreve todos os dados agora com os novos dados
    with open(dadosDB, "w") as f:
        json.dump(todosOsRegistros, f)


# * Carrega dados fictícios no sistema e salva no JSON.
def load_moc(dadosDB):
    # 1: Pega o caminho de onde esta o mock
    caminho_mock = "Data/mock.json"
    
    # 2: Verifica se o arquivo existe
    if os.path.exists(caminho_mock):
        # 3: abre o arquivo, e o ler
        with open(caminho_mock, "r") as dados:
            # 4: Carrega o Json com os dados do arquivo de mock na variavel "dadosMock", transformando ele num array multidimencional
            dadosMock = json.load(dados)

        # 5: Verifica que os dados são uma lista
        if isinstance(dadosMock, list):
            # 6: Percorre por toda a lista salvando os dados 1 por vez até o fim do Mock
            for usuario in dadosMock:
                # 6.1: Salva os dados usando o "save_data()"
                save_data(usuario, dadosDB)
        # 7: Retorna uma mensagem de "criado com sucesso" (201) 
        return jsonify({
            "message": "MOCK de dados carregado com sucesso!", 
            "usuarios": dadosMock}), 201
    
    # Se o arquivo de mock não existir ele somente retorna um erro
    else:
        return jsonify({
            "Erro" : "MOCK de dados fictios não existe"
        }), 404


