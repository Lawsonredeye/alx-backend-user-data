#!/usr/bin/env python3
"""Flask app for implementing RESTAPI
"""

from flask import Flask
from flask import jsonify
from auth import Auth
from flask import request

AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Home page for route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """registers new users into the db with its password hashed
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
