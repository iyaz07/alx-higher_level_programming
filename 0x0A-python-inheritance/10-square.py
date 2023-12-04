#!/usr/bin/python3
"""
This module provides the class "Square".
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """This is an class that inherit from Rectangle"""

    def __init__(self, size):
        """Creates a square with size validated"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)
