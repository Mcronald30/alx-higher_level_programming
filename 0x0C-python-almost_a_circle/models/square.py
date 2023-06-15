#!/usr/bin/python3
"""Creating Square Class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define the Square of the rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square of the rect"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """overloading __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
