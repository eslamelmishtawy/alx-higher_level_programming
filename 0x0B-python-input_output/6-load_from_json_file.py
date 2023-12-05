#!/usr/bin/bash
"""
file module
"""
import json


def load_from_json_file(filename):
    """
    save to json
    """
    with open(filename) as file:
        return json.load(f)
