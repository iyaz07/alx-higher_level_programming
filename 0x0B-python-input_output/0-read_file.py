#!/usr/bin/python3
"""
This module provides the function "read_file".
"""


def read_file(filename=""):
    """
    This function reads a file and prints it to the stdout.
    """


    with open(filename, 'r', encoding="UTF-8") as fd:

        for a in fd:
            print(a, end='')
