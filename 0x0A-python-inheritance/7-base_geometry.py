#!/usr/bin/python3
"""
Basegeometry Integer validator
"""


class BaseGeometry:
    """
    Module Class
    """
    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """
        Public instance method
        integer_validator
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
