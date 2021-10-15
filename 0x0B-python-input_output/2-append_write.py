#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """git file to write to and to append to"""

    with open(filename, "a") as appendfile:
        appendfile.write(text)
    return (len(text))
