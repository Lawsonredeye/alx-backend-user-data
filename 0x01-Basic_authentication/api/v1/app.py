#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth = os.getenv("AUTH_TYPE")
if auth == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth != "basic_auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """Handler for case where an auth is passed and has to be validated
    Raises:
        Aborts when the header is not found
    """
    path_list: list[str] = ['/api/v1/status/',
                            '/api/v1/unauthorized/', '/api/v1/forbidden/']
    path: str = request.path
    if auth.require_auth(path, path_list):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> tuple:
    """Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Forbidden access to api handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
