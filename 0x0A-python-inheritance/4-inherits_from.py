#!/usr/bin/python3
"""
This module stores the function "inherits_from".
"""


def inherits_from(obj, a_class):
    """
    This is a function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
