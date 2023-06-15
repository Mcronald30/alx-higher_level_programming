#!/usr/bin/python3
"""
Class Base Module
"""


class Base:
    """Define the class base"""
    __nb_objects = 0


    def __init__(self, id=None):
        """initializing the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
