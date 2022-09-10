#!/usr/bin/python3
"""add stuff"""



import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
loadFile.extend(sys.argv[idx] for idx in range(1, argc))
save_to_json_file(loadFile, "add_item.json")
