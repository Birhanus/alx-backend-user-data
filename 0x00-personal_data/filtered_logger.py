#!/usr/bin/env python3
"""module for personal data"""
import re


def filter_datum(fields: str, redaction: str, message: str,
                 separator: str) -> str:
    """fuction called filter_datum that retun the log message obfuscated"""
    for a in fields:
        data = re.sub(f'{a}=.*?{separator}',
                      f'{a}={redaction}{separator}', message)
    return data
