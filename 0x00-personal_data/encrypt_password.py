#!/usr/bin/env python3
"""
Module which has methods to has and validate hashed salted string
simulating a hashed protected password.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Encodes a string into a byte string and then salt hash a string
    into a byte encryt string
    """
    passwd: bytes = password.encode()
    crypt: bytes = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return crypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password password is equal to hashed password equals
    the byte encrypt password using byte password
    """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    return False
