#!/usr/bin/env python3
"""Hashing module for handling password protection
"""

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """encrypt string using UTF-8 encoding and returning a
    hashed salted byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers user into the the db but checks if email has already
        been used """
        if self._db.find_user_by(email=email):
            raise ValueError(f"User {email} already exists")
        else:
            hash_pwd = _hash_password(password)
            user = self._db.add_user(email, hash_pwd)
            return user
