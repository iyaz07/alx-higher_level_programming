#!/usr/bin/python3
"""
This is the module that provides the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    This is a function that returns True if the object is
    exactly an instance of the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False