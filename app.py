import os

from flask import Flask, render_template

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    from tasks.models import Task


    app = Flask(__name__)
    @app.route('/')
    def index():
        return '<h1>ECM Bonjour</h1>'

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.route('/todoz')
    def my_api_route():
        tasks = Task.query.all()
        return {
            "results": [
                {
                    field: getattr(task, field)
                    for field in Task.__table__.columns.keys()
                }
                for task in tasks
            ]
        }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)

    Migrate(app, db)
    return app