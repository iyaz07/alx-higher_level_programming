#!/usr/bin/python3
"""My Module Stores child class MyList"""


class MyList(list):
    """
    This is an object that inherits the list built-in object.
    The object has a print_sorted instance method that prints
    the contents of the list in ascending order.
    """
    def print_sorted(self):
        print(sorted(self))
