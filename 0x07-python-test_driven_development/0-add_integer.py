#!/usr/bin/python3
"""
Defines a function add_integer(a, b=98)
Return:
    sum a + b
"""


def add_integer(a, b=98):
    """Args:
        a (int): First value
        b (int, optional): Second value. Defaults to 98."""
    
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
