#!/usr/bin/python3
"""
this script creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    args:
    filename -> file path of type string
    """
    with open(filename, 'r') as fob:
        data = json.load(fob)
    return data
