from app import app

from flask import Flask


def test_app():
    assert app is not None
    assert isinstance(app, Flask)
