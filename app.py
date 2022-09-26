import os

from flask import Flask, render_template

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return '<h1>ECM Bonjour</h1>'

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)
    @app.route('/professor')
    def my_api_route():
        return {
            "name": "Adrien",
            "birthday": "02 January",
            "age": 85,
            "sex": None,
            "friends": ["Amadou", "Mariam"]
        }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)

    from tasks.models import Task

    Migrate(app, db)
    return app