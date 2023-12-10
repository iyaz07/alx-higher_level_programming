#!/usr/bin/python3
"""
The square class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """
        string representation
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Sets the width as a private attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """To check and set the value of the width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates a values of a square class using args and kwargs"""
        if len(args) == 0:
            for string, value in kwargs.items():
                self.__setattr__(string, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass

    def to_dictionary(self):
        """
        converts to dictionary
        """
        sqr_dict = {'id': self.id, 'x': self.x, 'size': self.width}
        sqr_dict['y'] = self.y
        return sqr_dict
