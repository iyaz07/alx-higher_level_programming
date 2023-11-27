#!/usr/bin/python3
# Iyaz

"""
This module supplies the function "text_indentation"
"""


def text_indentation(text):
    """
    Prints a string but prints 2 new line 
    at each occurence of ".", ":" and "?"i

    parameters:
        text (str): The text to read through.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        return
    for char in text:
        print("{}".format(char), end="")
        if char == "." or char == "?" or char == ":":
            print("\n")
