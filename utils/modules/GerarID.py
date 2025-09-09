# Biblioteca
# * Optei por usar o uuid para gerar os ID's porque creio que fique mais fidedigno a um projeto real
import uuid

# Import do Modulo para carregar os dados
from utils.modules.ManipulacaoDeDados import load_data

# ! A sobrecarga de metodo/parametro "dadosDB" EM TODAS as funções deve ser preenchida com a variavel "DADOSBD" do arquivo APP.PY, pois ele ira interagir com o arquivo "allData.json".
# * Esta função cria um ID completamente unico no padrão "uuid4"
def gerarID(dadosBD, key="id"):
    # 1: Carrega todos os dados do BD e os armazena
    dadosParaVerificacao = load_data(dadosBD)

    # 2: Se não houver dados, inicializa como lista
    if not isinstance(dadosParaVerificacao, list):
        dadosParaVerificacao = []

    # 3: Verifica e armazena todos os ID's existentes no banco de dados
    idsExistentes = {
        str(item.get(key)) for item in dadosParaVerificacao if isinstance(item, dict)
    }

    # 4: Gera um novo ID
    idNovo = str(uuid.uuid4())

    # 5: Verifica se o novo ID já existe comparando ele com todos os ID's que foram copiados
    while idNovo in idsExistentes: # 5.1 Garantir que os ID não se repita
        idNovo = str(uuid.uuid4()) # 6: Ele somente saira do loop apartir do momento que o ID for unico!
    
    return idNovo # 7: Retorna o ID novo