#!/usr/bin/env python3
"""Flask app for implementing RESTAPI
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Home page for route"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
