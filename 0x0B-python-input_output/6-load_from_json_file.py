#!/usr/bin/python3
"""
This module contains the function "load_from_json_file".
"""


import json


def load_from_json_file(filename):
    """
    This function creates an Object from a JSON file
    """

    with open(filename, encoding="UTF-8") as f:
        js = f.read()
    return json.loads(js)
