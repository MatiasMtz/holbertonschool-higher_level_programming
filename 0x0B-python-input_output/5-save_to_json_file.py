#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function that appends a string at the end of a text file (UTF8) and
returns the number of characters added"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
