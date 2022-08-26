#!/usr/bin/env python3
"""basic auth module"""
from api.v1.auth.auth import Auth
from flask import Flask, request
import re


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """return Base64 parht of the Authorizaiton
           header for A Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if re.search("^Basic ", authorization_header):
            return authorization_header[6:]
        else:
            return None
