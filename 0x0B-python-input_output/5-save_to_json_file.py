#!/usr/bin/bash
"""
file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
