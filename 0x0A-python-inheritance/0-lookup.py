#!/usr/bin/python3

__author__ = "Reganmatics"
"""0-lookup.py"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return [x for x in dir(obj)]
