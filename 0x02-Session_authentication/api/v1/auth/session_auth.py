#!/usr/bin/env python3
"""Session Auth that inherits from the Auth to protect users
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """"Childclass for Auth which handles new auth
    Mechanisim"""
    pass
