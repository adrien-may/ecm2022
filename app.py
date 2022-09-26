from flask import Flask, render_template


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

    return app