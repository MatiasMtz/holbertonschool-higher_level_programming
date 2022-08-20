#!/usr/bin/python3
"""get X-Request-Id header and display it"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
