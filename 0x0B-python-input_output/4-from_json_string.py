#!/usr/bin/python3
"""
This module supplies the function "from_json_string".
"""


import json


def from_json_string(my_str):
    """
    This function converts json string to object
    """

    return json.loads(my_str)
