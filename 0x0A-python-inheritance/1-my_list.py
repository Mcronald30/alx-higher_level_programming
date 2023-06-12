#!/usr/bin/python3
"""
Creating MyList
"""


class MyList(list):
    """
    MyList class that inherits from list
    """


    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        return print(sorted(self))
