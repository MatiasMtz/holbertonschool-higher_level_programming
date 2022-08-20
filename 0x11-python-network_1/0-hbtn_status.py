#!/usr/bin/python3
"""get intranet status and display it using urllib"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
