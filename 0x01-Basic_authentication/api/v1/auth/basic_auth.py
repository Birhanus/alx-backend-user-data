#!/usr/bin/env python3
"""basic auth module"""
from api.v1.auth.auth import Auth
from flask import Flask, request


class BasicAuth(Auth):
    """Basic auth class"""
