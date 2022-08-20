#!/usr/bin/python3
"""send an email to a url and display the body returned"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    res = requests.post(url, value)
    print(res.text)
