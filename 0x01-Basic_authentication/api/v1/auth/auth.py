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
        # print("path", path)
        # print("excluded:", excluded_paths)
        if path is None or excluded_paths is None:
            return True
        if excluded_paths is []:
            return True
        if path.endswith('/') is False:
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns an authorized header
        """
        if request is None:
            return None
        if request.headers.get("Authorization", None) is None:
            return None
        else:
            return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """checks current user
        """
        if request is None or request is []:
            return None

class BasicAuth(Auth):
    """Inherits from the Auth
    """
