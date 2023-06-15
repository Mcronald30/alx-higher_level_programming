#!/usr/bin/python3
"""Creating Rectangle Class"""


import json
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x coordinate"""
        self.__x = value

    @property
    def y(self):
        """y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y coordinate"""
        self.__y = value
