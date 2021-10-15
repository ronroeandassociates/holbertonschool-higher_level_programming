#!/usr/bin/python3
"""load_from_json"""
import json


def load_from_json_file(filename):
    """returns creates an Object from a JSON file"""

    with open(filename, "r") as readfile:
        return json.load(readfile)
