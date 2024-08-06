#!/usr/bin/env python3
"""Basic auth module which handles and uses base64 for params
"""
from api.v1.auth.auth import Auth


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
