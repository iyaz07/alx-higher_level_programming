#!/usr/bin/python3
"""
This module supplies the function "append_write".
"""


def append_write(filename="", text=""):
    """
    This function appends to a file
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        a = f.write(text)
    return a
