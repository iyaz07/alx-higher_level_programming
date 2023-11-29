#!/usr/bin/python3
# 4-print_square.py
# Iyaz
"""
This is the "4-print_square" module.
It performs one function, print_square(size).
"""


def print_square(size):
    """
    Prints the names
    parameters:
        size (int): The size of the square to prints

    Raises:
        TypeError: If `size` isn't integer.
        ValueError: If `size` is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
                print("#" * size)
