
# ! Este arquivo deve ser executado em um terminal separado ao terminal que esta rodando a API
# ! Dentro deste script, sera executados testes automatizados para checar todas as funcionabilidades da API de forma mais pratica, comprovando e testando seu funcionamento.

# Biblioteca
import requests

# URL da API
BASE_URL = "http://127.0.0.1:5000" # TODO: Se o endereço da API mudar quando for executada, ou voce estiver utilizando o Docker, altere aqui antes de rodar

# * Testar Mock
def test_mock():
    res = requests.post(f"{BASE_URL}/mocValcann")
    if res.status_code == 201:
        print(f"Teste MOCK Passou! {res.status_code} ✅")
    else:
        print(f"Teste MOCK Falhou! {res.status_code} 🚫")


# * ======== TESTES DO POST ========

# Cenario 1 (Dados todos Certos):  
def test_register_user1():
    registroNovo = {
        "name": "Monkey D. Luffy",
        "role" : "pirate",
        "email" : "eusouoR3iDosP1r4t4s@gmail.com",
        "page": {
                "page_size": 20,
                "pageActual": 2
                }
    }
    res = requests.post(f"{BASE_URL}/users/", json=registroNovo)
    if res.status_code == 201:
        print(f"Teste POST (Cenario1) Passou! {res.status_code} - Registrado com Sucesso ✅")
    else:
        print(f"Teste POST (Cenario1) Falhou! {res.status_code} - Não foi possivel efetuar o Registro 🚫")

# Cenario 2 (Email Repetido com registro aterior):  
def test_register_user2():
    registroNovo = {
        "name": "Buggy, o Palhaço Estrela",
        "role" : "pirate", 
        "email": "eusouoR3iDosP1r4t4s@gmail.com",
        "page": {
                "page_size": 30,
                "pageActual": 2
                }
    }
    res = requests.post(f"{BASE_URL}/users/", json=registroNovo)
    if res.status_code == 409:
        print(f"Teste POST (Cenario2) Passou! {res.status_code} - O Email não passou porque está duplicado ✅🤡")
    else:
        print(f"Teste POST (Cenario2) Falhou! {res.status_code} - O Email foi registrado 🚫")

# Cenario 3 (page_size > 50):  
def test_register_user3():
    registroNovo = {
        "name": "Dante Alighieri",
        "role" : "writer", 
        "email": "adivinaCOMEDIAHAHAHAH@gmail.com",
        "page": {
                "page_size": 60,
                "pageActual": 2
                }
    }
    res = requests.post(f"{BASE_URL}/users/", json=registroNovo)
    if res.status_code == 201:
        httpResponseJson = res.json()
        pageSizeTamanhoFinal = httpResponseJson['usuario']['page']['page_size']

        if pageSizeTamanhoFinal == 10:
            print(f"Teste POST (Cenario3) Passou! {res.status_code} - O Registro foi feito com o page_size em default (10) ✅")
        else:
            print(f"Teste POST (Cenario3) Falhou! {res.status_code} - page_size ficou em {pageSizeTamanhoFinal} 🚫")
    else:
        print(f"Teste POST (Cenario3) Falhou! {res.status_code} - O Email não foi registrado 🚫")

# Cenario 4 (pageActual > page_size):  
def test_register_user4():
    registroNovo = {
        "name": "Dr. Gregory House",
        "role" : "medic", 
        "email": "vicodin123@gmail.com",
        "page": {
                "page_size": 20,
                "pageActual": 30
                }
    }
    res = requests.post(f"{BASE_URL}/users/", json=registroNovo)
    if res.status_code == 201:
        httpResponseJson = res.json()
        
        pageActualTamanhoFinal = httpResponseJson['usuario']['page']['pageActual']
        pageSizeTamanhoFinal = httpResponseJson['usuario']['page']['page_size']

        if pageActualTamanhoFinal < pageSizeTamanhoFinal:
            print(f"Teste POST (Cenario4) Passou! {res.status_code} - O Registro foi feito com o pageActual em default (1) ✅")
        else:
            print(f"Teste POST (Cenario4) Falhou! {res.status_code} - pageActual ficou em {pageActualTamanhoFinal} 🚫")
    else:
        print(f"Teste POST (Cenario4) Falhou! {res.status_code} - O Email não foi registrado 🚫")

# Cenario 5 (pageActual > page_size & page_size > 50):  
def test_register_user5():
    registroNovo = {
        "name": "Simon Riley",
        "role" : "military", 
        "email": "eunaosouoGh0sT@gmail.com",
        "page": {
                "page_size": 100,
                "pageActual": 150
                }
    }
    res = requests.post(f"{BASE_URL}/users/", json=registroNovo)
    if res.status_code == 201:
        httpResponseJson = res.json()
        
        pageActualTamanhoFinal = httpResponseJson['usuario']['page']['pageActual']
        pageSizeTamanhoFinal = httpResponseJson['usuario']['page']['page_size']

        if pageActualTamanhoFinal == 1 and pageSizeTamanhoFinal == 10 :
            print(f"Teste POST (Cenario4) Passou! {res.status_code} - O Registro foi feito com o pageActual em default (1) e com o page_size em default (10) ✅")
        else:
            print(f"Teste POST (Cenario4) Falhou! {res.status_code} - pageActual ficou em {pageActualTamanhoFinal} e o page_size ficou em {pageSizeTamanhoFinal} 🚫")
    else:
        print(f"Teste POST (Cenario4) Falhou! {res.status_code} - O Email não foi registrado 🚫")



# * ======== TESTES DO GET ========

# Buscar todos os Registros
def test_get_all():
    res = requests.get(f"{BASE_URL}/users/all")
    if res.status_code == 200:
        print(f"Teste GET - TODOS OS REGISTROS Passou! {res.status_code} - Registrado com Sucesso ✅")
    else:
        print(f"Teste GET - TODOS OS REGISTROS Falhou! {res.status_code} - Não foi possivel buscar os Registros 🚫")

# Buscar Registros => Cenario 1:
def test_find_user():
    parametros = {
        "name": "Monkey D. Luffy",
        "email": "eusouoR3iDosP1r4t4s@gmail.com"
        }
    
    res = requests.get(f"{BASE_URL}/users/find/", params=parametros)
    if res.status_code == 200:
         print(f"Teste GET - Buscar Registro => Cenario 1 Passou! {res.status_code} - Registro encontrado com Sucesso ✅")
    else:
        print(f"Teste GET - Buscar Registro => Cenario 1 Falhou! {res.status_code} - Não foi possivel buscar o Registro 🚫")



# * ======== TESTES DO PUT ========

# Atualizar dado => gerado pelo mock.json
def test_update_user1():
    ID = 1
    dadosAtualizados = {
        "name": "Daniel", 
        "role" : "developer", 
        "email": "supercitzen@gmail.com", 
        "page": {
            "page_size": 30
            }
        }
    res = requests.put(f"{BASE_URL}/users/update/{ID}", json=dadosAtualizados)
    
    if res.status_code == 200:
        registroAtualizado = res.json()

        dadosUsuario = registroAtualizado.get('usuario', {})

        nomeAtualizado = dadosUsuario["name"]
        emailAtualizado = dadosUsuario['email']
        pageSizeAtualizado = dadosUsuario['page']['page_size']

        if (nomeAtualizado == dadosAtualizados["name"] and 
            emailAtualizado == dadosAtualizados["email"] and 
            pageSizeAtualizado == dadosAtualizados["page"]["page_size"]):
            print(f"Teste UPDATE - ATUALIZAR DADO Passou! {res.status_code} - Registro atualizado com Sucesso ✅ ")
        else:
            print(f"Teste UPDATE - ATUALIZAR DADO Falhou! {res.status_code} - Registro não foi atualizado. 🚫 ")
    else:
        print(f"Teste UPDATE - ATUALIZAR DADO Falhou! {res.status_code} - Registro não foi encontrado. 🚫 ")

# Não atualizar dado (Dado não encontrado)
def test_update_user2():
    ID = 'fc571b9a-f41'
    dadosAtualizados = {
        "name": "My Head Is Empty", 
        "role" : "artist", 
        "email": "mirandaRain@gmail.com", 
        "page": {
            "page_size": 20
            }
        }
    res = requests.put(f"{BASE_URL}/users/update/{ID}", json=dadosAtualizados)
    if res.status_code == 404:
        print(f"Teste UPDATE - ATUALIZAR DADO (Não atualizar dado) Passou! {res.status_code} - Registro não foi encontrado. ✅ ")
    else:
        print(f"Teste UPDATE - ATUALIZAR DADO (Não atualizar dado) Falhou! {res.status_code} - Registro atualizado. 🚫 ")

# * ======== TESTES DO DELETE ========

# Cenario 1: Dado Existe e foi excluido
def test_delete_user1():
    ID = 2
    res = requests.delete(f"{BASE_URL}/users/{ID}")
    if res.status_code == 200:
        print(f"Teste DELETE - EXCLUIR DADO Passou! {res.status_code} - Registro apagado do sistema. ✅ ")
    else:
        print(f"Teste DELETE - ATUALIZAR DADO Falhou! {res.status_code} - Registro não foi apagado do sistema. 🚫 ")


# Cenario 2: Dado não existe e não pode ser excluido
def test_delete_user2():
    ID = "2"
    res = requests.delete(f"{BASE_URL}/users/delete/{ID}")
    if res.status_code == 404:
        print(f"Teste DELETE - Dado não existe Passou! {res.status_code} - Registro não foi apagado do sistema. ✅ ")
    else:
        print(f"Teste DELETE - Dado não existe Falhou! {res.status_code} - Algum registro com esse ID apagado do sistema . 🚫 ")

# * ======== EXECUÇÃO DOS TESTES ========

if __name__ == "__main__":
    test_mock()
    test_register_user1()
    test_register_user2()
    test_register_user3()
    test_register_user4()
    test_register_user5()
    test_get_all()
    test_find_user()
    test_update_user1()
    test_update_user2()
    test_delete_user1()
    test_delete_user2()