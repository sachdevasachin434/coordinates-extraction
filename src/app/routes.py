"""
    Module for initialising routes for project.
"""
from flask_restx import Api
from .extract.controller import API as extract_api


def register_routes(api: Api):
    """Method for registering route for API

    Args:
        api (flask_restx.Api): Flask-RestX's default API class
        root (str, optional): root route for endpoints. Defaults to 'api'.
    """

    api.add_namespace(extract_api, path="/")
