#!/usr/bin/env python3
"""Template for all authentication system to be implemented
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication object which is used for authentication
    and uses the flask_request as an object
    """
    def require_auth(self, path: str, excluded_paths: List[str]):
        """checks for auth and returns false"""
        if path is None and excluded_paths is None or []:
            return True
        if path in excluded_paths:
            return False
        elif path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """returns an authorized header
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """checks current user
        """
        return request
