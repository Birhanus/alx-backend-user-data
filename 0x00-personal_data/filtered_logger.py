#!/usr/bin/env python3
"""module for personal data"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """fuction called filter_datum that retun the log message obfuscated"""
    for a in fields:
        data = re.sub(f'{a}=.*?{separator}',
                      f'{a}={redaction}{separator}', message)
    return data


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
