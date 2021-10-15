#!/usr/bin/python3
""" lets write a file """


def write_file(filename="", text=""):
    """ read the file and write it """
    
    with open(filename, "w") as writefile:
        writefile.write(text)
    return (len(text))
