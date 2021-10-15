#!/usr/bin/python3
""" sve_JSON """
import json


def save_to_json_file(my_obj, filename):
    """ write object to txt using json """
    with open(filename, "w") as savefile:
        json.dump(my_obj, savefile)
