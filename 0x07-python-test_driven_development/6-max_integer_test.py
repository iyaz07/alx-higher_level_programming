#!/usr/bin/python3
# 0-add_integer.py
# Iyaz
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """
        Parameters:
            list (list): A list of integers.

        Returns:
            Returns the highest list[i]
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
