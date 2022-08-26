"""Auth module"""

from flask import Flask, request
from typing import List,  TypeVar


class Auth:
    """calss to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        return False

    def authorization_header(self, reuest=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return current user"""
        return None
