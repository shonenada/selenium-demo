from flask import Flask

from demo.views import master_app


def create_app(name=None):
    app = Flask(name or __name__)
    app.register_blueprint(master_app)
    return app
