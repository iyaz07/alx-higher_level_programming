#!/usr/bin/python3
"""
This module provides the class "Square".
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from the base class "Rectangle"
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
