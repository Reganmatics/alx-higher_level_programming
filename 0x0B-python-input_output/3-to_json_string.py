#!/usr/bin/python3
"""
this script returns the json representation of an object
"""
import json


def to_json_string(my_obj):
    """
    args:
        my_obj -> string object
    """
    return json.dumps(my_obj)
