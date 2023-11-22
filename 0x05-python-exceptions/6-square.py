#!/usr/bin/python3
# 6-square.py
# By Iyaz


class Square:
    """Define a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """A construction size and position as argument"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """To check for the type and value and raise if either is false"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """The properities of the size of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """To check if position is a tuple containing 2 positive integers"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not ((isinstance(value[0], int)) and (isinstance(value[1], int))):
            raise TypeError('position must be a tuple of 2 positive integers')
        if ((value[0] < 0) or (value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """A Construction for the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """A construction used to print a square with length of size"""
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
