#!/usr/bin/python3
"""Define Square by size"""


class Square:
    """definition size and verification"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

    @property
    def size(self):
        """is the size of property"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    """def square of area"""

    def area(self, size=0):
        return self.__size ** 2
