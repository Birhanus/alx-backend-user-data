#!/usr/bin/env python3
"""Session Authentication"""
from .auth import Auth
from uuid import uuid4
from flask import request
from models.user import User


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

    def current_user(self, request=None) -> User:
        """method that returns a User instance based on cookiew value"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """logout deletes the user session"""
        session_id = self.session_cookiew(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
