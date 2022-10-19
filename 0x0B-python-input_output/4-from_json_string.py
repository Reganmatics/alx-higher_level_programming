#!/usr/bin/python3
"""
this script returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    args:
        my_atr -> string to deserialize to python object
    """
    return json.loads(my_str)
