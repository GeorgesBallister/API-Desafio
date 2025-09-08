# Bibliotecas
from flask import Flask, request, jsonify
import os
import json
# ! A sobrecarga de metodo/parametro "dadosDB" deve ser preenchida com o DADOSBD do arquivo APP.PY.

# Carrega os dados do arquivo JSON "allData.json"
def load_data(dadosDB):
    # Abre Arquivo no caminho que sera fornecido pelo "DADOSDB"
    if os.path.exists(dadosDB):
        # Le o arquivo
        with open(dadosDB, "r") as f:
            return json.load(f)
    else:
    # Se não existir dados retorna uma mensagem
        return "Sem Dados"

def save_data(data, dadosDB):
    # Abre o arquivo "allData.json" como escrita 
    with open(dadosDB, "w") as f:
    # Pega os dados json armazenados em uma variavel, dos quais serão representados pelo parametro "data" e faz um dump a baixo dos dados já existentes
        json.dump(data, f)


def load_moc(dadosDB):
    # Carrega dados fictícios no sistema e salva no JSON.
     caminho_mock = "Data/mock.json"
    
    # Verifica se o arquivo existe no caminho
     if os.path.exists(caminho_mock):
        # Abre o Arquivo, lê e referencia como "f"
        with open(caminho_mock, "r") as f:
           # Salva o conteudo do arquivo nessa variavel
           userMock = json.load(f)
           # Salva no banco de dados tudo
           save_data(userMock, dadosDB)
           return jsonify({"message": "MOC de dados carregado com sucesso!", "usuarios": userMock}), 201
     else:
    # Se não existir o arquivo retorna uma mensagem
        return jsonify({"message": "MOC de dados não existe"}), 201

