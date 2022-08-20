#!/usr/bin/python3
"""takes in a letter and sends a POST request and display the content"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    body = {'q': ""}
    if len(sys.argv) > 1:
        body['q'] = sys.argv[1]

    res = requests.post(url, body)
    try:
        json_data = res.json()
        if 'id' in json_data and 'name' in json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
