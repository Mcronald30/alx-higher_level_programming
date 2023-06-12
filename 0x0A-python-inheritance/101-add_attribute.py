#!/usr/bin/python3
"""
New attribute
"""

def add_attribute(obj, attribute, value):
    """
    a function that adds a new attribute
    to an object if it’s possible
    """
    if not hasattr(obj, "__dict__"):
        """
        The function first checks if
        the obj has a __dict__ attribute
        """
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute] = value
