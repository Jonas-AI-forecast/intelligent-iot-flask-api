from app import add

def test_add():
    assert add(2, 3) == 5

def test_hello():
    from app import app
    response = app.test_client().get("/hello")
    assert response.status_code == 200
    assert response.get_json()["version"] == 2
