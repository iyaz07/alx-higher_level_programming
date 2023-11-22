#!/usr/bin/python3
# 3-square.py
# Iyaz
"""Define a class Square."""


class Square(object):
    """class variable size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define the area of a square"""
        return self.__size * self.__size
