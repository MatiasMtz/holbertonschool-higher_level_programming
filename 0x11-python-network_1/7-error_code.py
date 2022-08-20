#!/usr/bin/python3
"""send a get request to a url provided and handle error"""
import requests
import requests.exceptions
import sys


if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as error:
        print("Error code: {}".format(error.response.status_code))
