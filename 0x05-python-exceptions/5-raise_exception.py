#!/usr/bin/python3
def raise_exception():
    raise TypeError("Exception raised")

# Test the function with the provided example
try:
    raise_exception()
except TypeError as te:
    print(str(te))

