import os

from flask import Flask

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>ECM Bonjour</h1>"

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config['API_TITLE'] = 'My ECM API'
    app.config["API_VERSION"] = "1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/openapi"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    api = Api(app)

    from tasks.views import task_blueprint

    api.register_blueprint(task_blueprint)

    return app