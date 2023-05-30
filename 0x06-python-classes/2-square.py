#!/usr/bin/python3
""" Creating a square class """

class Square:
    """ Defining a class square """
    def __init__(self, size=0):
        """Initialises the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
