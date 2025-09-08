# Bibliotecas
from flask import Flask, request, jsonify
import os
import json
# ! A sobrecarga de metodo/parametro "dadosDB" deve ser preenchida com o DADOSBD do arquivo APP.PY.

# Carrega os dados do arquivo JSON "allData.json"
def load_data(dadosDB):
    if os.path.exists(dadosDB):
        with open(dadosDB, "r") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return []  # Arquivo vazio ou inválido → retorna lista vazia

        if isinstance(dados, dict):
            return [dados]
        elif isinstance(dados, list):
            return dados
        else:
            return []
    else:
        return []  # Se não existir, retorna lista vazia


def save_data(data, dadosDB):
    dadosAntigos = load_data(dadosDB)

    if not isinstance(dadosAntigos, list):
        dadosAntigos = []

    dadosAntigos.append(data)

    with open(dadosDB, "w") as f:
        json.dump(dadosAntigos, f, indent=4)

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



