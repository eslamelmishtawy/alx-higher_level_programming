#!/usr/bin/python3
"""
file module
"""


def write_file(filename="", text=""):
    """
    write file
    Args:
        filname
        text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
