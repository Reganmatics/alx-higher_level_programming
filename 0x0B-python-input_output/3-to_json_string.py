#!/usr/bin/python3

import json

"""
this script returns the json representation of an object
"""


def to_json_string(my_obj):
    """
    args:
        my_obj -> string object
    """
    return json.dumps(my_obj)
