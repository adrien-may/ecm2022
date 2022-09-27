from flask import Flask


def test_app(app):
    assert app is not None
    assert isinstance(app, Flask)


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "ECM" in response.get_data(as_text=True)
