import requests

BASE_URL = "http://localhost:5000"

def test_mock():
    res = requests.post(f"{BASE_URL}/moc")
    print("Mock:", res.status_code, res.json())

def test_register_user():
    payload = {
        "nome": "Bloom",
        "email": "georges@gmail.com",
        "page": {"page_size": 20, "pageActual": 2}
    }
    res = requests.post(f"{BASE_URL}/users/", json=payload)
    print("Register:", res.status_code, res.json())

def test_get_all():
    res = requests.get(f"{BASE_URL}/users/all")
    print("Get All:", res.status_code, res.json())

def test_find_user():
    params = {"nome": "Bloom", "email": "georges@gmail.com"}
    res = requests.get(f"{BASE_URL}/users/find/", params=params)
    print("Find User:", res.status_code, res.json())

def test_update_user():
    payload = {"nome": "Bloom", "email": "georges@gmail.com", "page": {"page_size": 30}}
    res = requests.put(f"{BASE_URL}/users/update/1", json=payload)
    print("Update:", res.status_code, res.json())

def test_delete_user():
    res = requests.delete(f"{BASE_URL}/users/delete/1")
    print("Delete:", res.status_code, res.json())


if __name__ == "__main__":
    test_mock()
    test_register_user()
    test_get_all()
    test_find_user()
    test_update_user()
    test_delete_user()
