#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter"""


import requests
import sys

if __name__ == "__main__":

    var = sys.argv[1] if len(sys.argv) == 2 else ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': var})
    try:
        dir_element = req.json()
        if len(dir_element) == 0:
            print("No result")
        else:
            print(f"[{dir_element['id']}] {dir_element['name']}")
    except ValueError:
        print("Not a valid JSON")
