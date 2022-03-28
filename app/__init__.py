from flask import Flask
from .config import initialize_config


def create_app():
    app = Flask(__name__)
    initialize_config(app)
    return app
