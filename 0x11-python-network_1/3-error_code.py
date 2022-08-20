#!/usr/bin/python3
"""send a get request to a url provided"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            body = res.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))
