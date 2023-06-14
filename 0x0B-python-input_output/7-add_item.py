#!/usr/bin/python3
"""
Load, add, save
"""


import sys
import json
from os import path


def save_to_json_file(my_obj, filename):
    """
    Write a script that adds all arguments
    to a Python list, and then save them to a file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


args = sys.argv[1:]


if path.exists('add_item.json'):
    items = load_from_json_file('add_item.json')
else:
    items = []

    items.extend(args)


    # Save updated list to file
    save_to_json_file(items, 'add_item.json')

