#!/usr/bin/python3
# 4-square.py
# By Mark Wonah
"""Define a class Square."""


class Square:
    """Class variable size"""
    def __init__(self, size=0):
        """Initialize size"""
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """A construction used to print a square with length of size"""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()
        if self.__size is 0:
            print()
