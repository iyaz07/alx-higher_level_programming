#!/usr/bin/python3
# Iyaz
"""
This module contains the class "Rectangle".
"""


class Rectangle:
    """This is a Rectangle with 2 integers representing length and width"""
    def __init__(self, width, height):
        self.height = height
        self.width = width

    @property
    def height(self):
        """Returns private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """check value type, else raise error"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
