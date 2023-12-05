#!/usr/bin/python3
"""
file module
"""


def read_file(filename=""):
    """
    read file
    Args:
        filname
    """
    with open(filename, encoding="utf-8") as f:
        f.read()
