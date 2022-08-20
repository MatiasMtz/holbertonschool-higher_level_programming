#!/usr/bin/python3
"""send an email to a url and display the body returned"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
