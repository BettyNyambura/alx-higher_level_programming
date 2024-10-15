#!/usr/bin/python3
"""add item"""


import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    try:
        obj = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        obj = []
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, filename)
