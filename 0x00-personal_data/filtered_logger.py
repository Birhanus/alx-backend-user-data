#!/usr/bin/env python3
"""module for personal data"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """fuction called filter_datum that retun the log message obfuscated"""
    for a in fields:
        message = re.sub(f'{a}=.*?{separator}',
                         f'{a}={redaction}{separator}', message)
    return message
