#!/usr/bin/env python3
"""Module which handles obfuscation"""
import re


def filter_datum(fields: str, redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate vital information in a string but splitting the string
    and filter through the string."""
    message = message.split(separator)
    new_message: list = []
    for mess in message:
        for field in fields:
            if re.search(field, mess):
                mess = f"{field}=" + re.sub(f"^({field}=[a-z0-9//]*)*",
                                            redaction, mess)
        new_message.append(mess)
    return f"{separator}".join(new_message)
