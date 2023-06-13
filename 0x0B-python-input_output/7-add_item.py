#!/usr/bin/python3
"""
Load, add, save
"""


import sys
import json


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

filename = "add_item.json"

# Load existing data from file
try:
    data = load_from_json_file(filename)
except:
    data = []

# Add command-line arguments to the list
data.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(data, filename)
