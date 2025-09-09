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
    
    if os.path.exists(caminho_mock):
        with open(caminho_mock, "r") as dados:
            dadosMock = json.load(dados)

        if isinstance(dadosMock, list):
            for usuario in dadosMock:
                save_data(usuario, dadosDB)
                
        return jsonify({
            "message": "MOCK de dados carregado com sucesso!", 
            "usuarios": dadosMock}), 201
    else:
        return jsonify({
            "Erro" : "MOCK de dados fictios não existe"
        }), 404


