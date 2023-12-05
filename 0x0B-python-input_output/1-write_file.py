#!/usr/bin/python3
"""Writing into a file"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, mode="w", encoding='utf-8') as f:
        return (f.write(text))
