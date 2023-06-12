#!/usr/bin/python3
"""
Creating Rectangle from Basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        initializing the variables and methods
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
