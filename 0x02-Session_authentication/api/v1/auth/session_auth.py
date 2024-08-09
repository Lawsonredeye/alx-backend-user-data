#!/usr/bin/env python3
"""Session Auth that inherits from the Auth to protect users
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """"Childclass for Auth which handles new auth
    Mechanisim"""
    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session for new users or loggin
        Returns:
        - string session id
        """
        if user_id == None or not isinstance(user_id, str):
            return None
        else:
            session_id: str = str(uuid.uuid4())
            self.user_id_by_session_id[user_id] = session_id
            return session_id
