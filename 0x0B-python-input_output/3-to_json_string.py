#!/usr/bin/python3
"""
This supplies the function "to_json_string".
"""


import json


def to_json_string(my_obj):
    """
    To convert an object to json string
    """
    return json.dumps(my_obj)
