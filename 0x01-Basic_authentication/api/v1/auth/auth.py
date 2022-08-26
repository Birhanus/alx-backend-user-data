"""Auth module"""
from flask import Flask, request
from typing import List,  TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, reuest=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
