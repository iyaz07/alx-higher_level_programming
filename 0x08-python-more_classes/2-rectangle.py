#!/usr/bin/python3
# Iyaz
"""
This is a module that supplies the class "rectangle".
"""


class Rectangle:
    """
    This is a class that initiates a rectangle construction.
    properties:
        width(int)
        height(int)i
        self.__height * self.__width
        2 * (self.__height + self.__width
    Returns:
        
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return (2 * (self.__height + self.__width))
