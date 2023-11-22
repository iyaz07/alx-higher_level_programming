#!/usr/bin/python3
# 2-square.py
# By Iyaz
"""Define a class square."""

class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """"A construction with private size as argument and raising error
        in 2 situations first if the type of size isnt an integer and second
        if the value of size is less than 0"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
