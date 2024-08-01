#!/usr/bin/env python3
"""Module which handles obfuscation
"""

import logging
import re


def filter_datum(fields: str, redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate vital information in a string but splitting the string
    and filter through the string."""
    messages: list[str] = message.split(separator)
    new_message: list = []
    for mess in messages:
        for field in fields:
            if re.search(field, mess):
                mess = f"{field}=" + re.sub(f"^({field}=[a-z0-9/@./-]*)*",
                                            redaction, mess)
        new_message.append(mess)
    return f"{separator}".join(new_message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple[str]):
        """class initializer
        """
        self.fields = list(fields)
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """converts the logging message into obfuscated data
        which would be protected"""
        messages = record.getMessage()
        filter: str = filter_datum(self.fields, self.REDACTION,
                                   messages, self.SEPARATOR)
        record.msg = filter
        return filter
