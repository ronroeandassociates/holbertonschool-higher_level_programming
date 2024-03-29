#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response"""


import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code < 400:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
