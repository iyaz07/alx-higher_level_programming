#!/usr/bin/python3
"""This Module stores the function Geometry"""


class BaseGeometry():
    """This is an empty BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exceptiom("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
