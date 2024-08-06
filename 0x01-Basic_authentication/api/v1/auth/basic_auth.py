#!/usr/bin/env python3
"""Basic auth module which handles and uses base64 for params
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """Inherits from the Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 string or value to be encoded for http
        """
        if not isinstance(authorization_header, str):
            return None
        if authorization_header is None or authorization_header == "":
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.lstrip("Basic ")

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Decode encoded base64 strings into strings
        Returns:
            Decoded base64 encoding into a string
        Raises:
            Exception when a string is being decoded instead of a byte-string
        """
        if base64_authorization_header is None:
            return None
        if base64_authorization_header == "":
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base = base64.b64decode(
                base64_authorization_header).decode("utf-8")
            return base
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """extracts users credentials from decoded Base64 value
        """
        decoded = decoded_base64_authorization_header

        if not isinstance(decoded, str):
            return None, None
        if decoded == "" or decoded is None:
            return None, None
        if decoded.find(":") < 0:
            return None, None
        email, password = decoded.split(":")
        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """checks user
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        if user_email == "" or user_pwd == "":
            return None

        user = User()
        if user.search({"email": user_email}) != user_email:
                return None
        # if user.search(user_email) is None:
        #         return None
        
        if user_pwd is not user.is_valid_password(user_pwd):
            return None
        return user
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Fetch current user
        """
        user = User()
        self.authorization_header(request.path)
        self.extract_base64_authorization_header(request)
        extract = self.decode_base64_authorization_header(extract)
        self.extract_user_credentials(extract)
        self.user_object_from_credentials(user)
