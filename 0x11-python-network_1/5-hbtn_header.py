#!/usr/bin/python3
"""get X-Request-Id header and display it"""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
