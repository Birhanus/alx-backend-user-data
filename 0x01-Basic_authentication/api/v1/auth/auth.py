#!/usr/bin/env python3
"""Auth module"""
from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """calss to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path in excluded_paths or path + "/" in excluded_paths:
            return False
        if path not in excluded_paths:
            return True
        for e_path in excluded_paths:
            if e_path.endswith('*'):
                if path.startswith(i[:1]):
                    return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """return current user"""
        return None
