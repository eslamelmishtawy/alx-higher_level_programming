#!/usr/bin/python3
"""
My list module
"""


class Mylist(list):
    """
    My list class
    """
    def __init__(self):
        pass

    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
