#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id)"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    try:
        req = requests.get(url, auth=HTTPBasicAuth(user, passwd))
        dir_element = req.json()
        print(dir_element['id'])
    except Exception:
        print("None")
