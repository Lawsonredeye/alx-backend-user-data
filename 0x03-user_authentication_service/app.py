#!/usr/bin/env python3
"""Flask app for implementing RESTAPI
"""

from flask import Flask
from flask import jsonify, abort
from auth import Auth
from flask import request, Response

AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Home page for route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> Response:
    """registers new users into the db with its password hashed
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"])
def login():
    """Handles user login by validating email
    Returns:
    Bool
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        res = AUTH.valid_login(email, password)
        return jsonify({"email": email, "message": "logged in"})
    except Exception as e:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
