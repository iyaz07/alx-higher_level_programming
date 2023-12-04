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


class Rectangle(BaseGeometry):
    """This is an class that inheret from Base Geometry"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
