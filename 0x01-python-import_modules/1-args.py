#!/usr/bin/python3
import sys


def main(*argv):
    l = len(sys.argv) - 1
    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
    else:
        print("{:d} arguments:".format(l))
    for i, args in enumerate(sys.argv):
        if (i != 0):
            print(f"{i}: {args}")

if __name__ == "__main__":
    main()
