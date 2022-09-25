from app import app

from flask import Flask


def test_app():
    assert app is not None
    assert isinstance(app, Flask)

def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "ECM" in response.data.decode("utf-8")


def test_index_user():
    client = app.test_client()
    response = client.get("/user/adrien")
    assert response.status_code == 200
    result = response.data.decode("utf-8")
    assert "Hello, adrien" in result
