#!/usr/bin/python3
"""module to create a class named square"""


class Square:
    """define class and assign private attributes"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if tupe(value) is not int:
            raise TypeError("SIZE MUST BE AN INTEGER")

        elif value < 0:
            raise ValueError("SIZE MUST BE >=0")

        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()
