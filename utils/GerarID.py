# Biblioteca
import uuid

# Import do Modulo
from utils.ManipulacaoDeDados import load_data

def gerarID(dadosBD, key="id"):
    dadosParaVerificacao = load_data(dadosBD)

    # Se não houver dados, inicializa como lista
    if not isinstance(dadosParaVerificacao, list):
        dadosParaVerificacao = []

    idsExistentes = {
        str(item.get(key)) for item in dadosParaVerificacao if isinstance(item, dict)
    }

    idNovo = str(uuid.uuid4())
    while idNovo in idsExistentes: # Garantir que os ID não se repita
        idNovo = str(uuid.uuid4()) 
    
    return idNovo