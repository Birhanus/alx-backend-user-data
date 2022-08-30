#!/usr/bin/env python3
"""Session Authentication"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class for session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""
        if user_id is None:
            return None
        if isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        else:
            return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method that returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        else:
            return None
