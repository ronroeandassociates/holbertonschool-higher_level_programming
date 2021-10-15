#!/usr/bin/python3
""" read_file """


def read_file(filename=""):
    """get file to read"""
    with open(filename, encoding="utf-8") as readfile:
        print(readfile.read(), end="")
