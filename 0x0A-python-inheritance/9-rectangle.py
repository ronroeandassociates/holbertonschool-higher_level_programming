#!/usr/bin/python3
"""Write a class that inherits from another class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
        """Defines the Rectangle class"""

        def __init__(self, width, height):
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height

        def area(self):
            return self.__height * self.__width

        def __str__(self):
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
