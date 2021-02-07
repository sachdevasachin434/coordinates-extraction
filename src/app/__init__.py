"""
    Main module for creating app.
"""
from flask import Flask
from flask_restx import Api
from .routes import register_routes


def create_app():
    """Creates the flask app to be run by ../main.py

    Returns:
        app [Flask]: The flask application to be run by main.py
    """
    app = Flask(__name__)
    api = Api(app)
    register_routes(api)

    return app
