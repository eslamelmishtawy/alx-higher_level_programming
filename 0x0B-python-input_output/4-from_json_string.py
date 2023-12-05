#!/usr/bin/python3
"""
file module
"""
import json


def from_json_string(my_str):
    """
    covert object to json
    Args:
        obj
    """
    return json.loads(my_str)
