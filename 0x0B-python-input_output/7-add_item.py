#!/usr/bin/python3
"""Load, add, save"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    _list = load_from_json_file(filename)
except FileNotFoundError:
    _list = []
for i in range(1, len(sys.argv)):
    _list.append(sys.argv[i])
save_to_json_file(_list, filename)
