#!/usr/bin/env python3
"""Hashing module for handling password protection
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """encrypt string using UTF-8 encoding and returning a
    hashed salted byte string
    """
    byte_pwd: bytes = password.encode()
    return bcrypt.hashpw(byte_pwd, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers user into the the db but checks if email has already
        been used """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_pwd = _hash_password(password)
            user: User = self._db.add_user(email, hash_pwd)
            return user
    
    def valid_login(self, email: str, password: str) -> bool:
        """locates and validate if user email exists and checks hashed
        password if it matches unhashed passord.
        Returns:
            Bool if the password matches or not"""
        try:
            user_found = self._db.find_user_by(email=email)
            hashed = password.encode("UTF-8")
            response = bcrypt.checkpw(hashed, user_found.hashed_password)
            return response
        except:
            return False


    def _generate_uuid(self) -> str:
        """UUID generator
        """
        return str(uuid.uuid4())
