#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    Write a function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
    """
    description = {}
    description['__class__'] = obj.__class__.__name__
    description['__attributes__'] = {}


    """Iterate over object attributes"""
    for attr, value in obj.__dict__.items():
        """Serialize simple data types
        (list, dictionary, string, integer, boolean)"""
        if isinstance(value, (list, dict, str, int, bool)):
            description['__attributes__'][attr] = value
            return description
