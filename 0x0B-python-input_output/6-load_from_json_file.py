#!/usr/bin/python3
"""
file module
"""
import json


def load_from_json_file(filename):
    """
    save to json
    """
    with open(filename) as f:
        return json.load(f)
