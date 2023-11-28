#!/usr/bin/python3
# Iyaz
"""
This is a module that supplies the class "rectangle".
"""


class Rectangle:
    """
    This is a class that initiates a rectangle construction.
    properties:
        width(int)
        height(int)i
        self.__height * self.__width
        2 * (self.__height + self.__width
    Returns:
        Area, perimeter, and # shape
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        shape = ""
        if self.__height == 0 or self.__width == 0:
            return shape
        for i in range(self.__height):
            for j in range(self.__width):
                shape += str(self.print_symbol)
            if i < self.__height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
