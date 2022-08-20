#!/usr/bin/python3
"""get github user id"""

import requests
import sys

if __name__ == "__main__":
    res = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    res_json = res.json()
    print(res_json.get('id'))
