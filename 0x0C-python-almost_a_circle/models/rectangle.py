#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height myst be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be >=0")
            self.__y = value

        def area(self):
            """area of rectangle"""
            return (self.__width * self.__height)

        def display(self):
            """display rectangle with ### """

            if self.__y != 0:
                for newline in range(self.y):
                    print()
                for row in range(self.__height):
                    print((self.__x * " ") + (self.__width * '#'))

        def __str__(self):
            """Returns formatted info display"""

            return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                    self.id, self.__x, self.__y,
                                                    self.__width, self.__height)
