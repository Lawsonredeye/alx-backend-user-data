#!/usr/bin/env python3
"""Basic auth module which handles and uses base64 for params
"""
from api.v1.auth.auth import Auth
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
