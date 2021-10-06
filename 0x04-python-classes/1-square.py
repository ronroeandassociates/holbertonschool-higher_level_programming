#!/usr/bin/python3
"""make a module with a class of square"""


class Square:
    """make it all about size and some private attributes"""
    def __init__(self, size=0)
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
