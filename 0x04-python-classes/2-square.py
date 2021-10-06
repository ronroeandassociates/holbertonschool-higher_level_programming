#!/usr/bin/python3
""" Define Square by size """


Class Square:
    """Define size with verification"""
    def__init__(self, size=0):        
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """Define area of square"""

        def area(self, size=0):
            sr_area = self.__size ** 2
            return sr_area