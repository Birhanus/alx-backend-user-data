#!/usr/bin/env python3
"""basic auth module"""
from api.v1.auth.auth import Auth
from flask import Flask, request
import re
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """return Base64 part of the Authorizaiton
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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string
           base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None
        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns the user email and password from the Base64
           decoded value.
        """
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ return User instance based on their email and password
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, requesst=None) -> TypeVar('User'):
        """retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
