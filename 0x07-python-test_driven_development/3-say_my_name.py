#!/usr/bin/python3
# 3-say_my_name.py
# Iyaz
"""
This module prints the full name of anything
The first name and last name must be a strings
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is" followed by the first name and optional last name
        parameters:
            first_name (str): A string
            last_name (str): A string

        Raises:
            TypeError is either parmeter isnt string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a stiring")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
