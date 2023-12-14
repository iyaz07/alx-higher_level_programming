#!/usr/bin/python3
"""
The Rectangle class module
"""


from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class
    """

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if isinstance(height, bool):
            self.__height = 1 if height else 0
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y getter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        calculate the area
        """
        return self.width * self.height

    def display(self):
        """
        displays rectangle with '#'
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Configure :string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Update a values of a rectangle class by assigning args and kwargs"""
        if len(args) == 0:
            for string, value in kwargs.items():
                self.__setattr__(string, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass

    def to_dictionary(self):
        """
        converts to dictionary
        """
        dic = {'id': self.id, 'width': self.width, 'height': self.height}
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
