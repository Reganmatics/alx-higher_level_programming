#!/usr/bin/python3
"""
this script uses JSON representation to write an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args:
    my_obj -> object of interest
    filename -> path to write to
    """
    with open(filename, mode='w', encoding="UTF8") as fob:
        json.dump(my_obj, fob)
