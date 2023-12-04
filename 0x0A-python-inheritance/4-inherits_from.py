#!/usr/bin/python3
"""
check inherits from module
"""

def inherits_from(obj, a_class):
    """
    check if object inherits from class
    Args:
        obj: an object
        class: class
    Return true or false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
