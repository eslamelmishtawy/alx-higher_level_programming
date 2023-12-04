#!/usr/bin/python3
"""
My list module
"""


class MyList(list):
    """
    My list class
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
