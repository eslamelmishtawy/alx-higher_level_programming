#!/usr/bin/python3
"""
file module
"""


def append_write(filename="", text=""):
    """
    write file append
    Args:
        filname
        text
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
