#!/usr/bin/env python3
"""module for encrypt user password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypted password"""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check valid password"""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
