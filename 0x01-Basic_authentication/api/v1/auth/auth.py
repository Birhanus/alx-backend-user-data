#!/usr/bin/env python3
"""Auth module"""
from flask import Flask, request
from typing import List,  TypeVar


class Auth:
    """calss to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        if path not in excluded_paths:
            return True

    def authorization_header(self, reuest=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return current user"""
        return None
