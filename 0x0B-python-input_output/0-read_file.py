#!/usr/bin/python3

"""
this script prints out text file to stdout
"""

def read_file(filename=""):
    """
    args:
        filename: string containing file path
    """

    with open(filename, encode="utf-8") as fob:
        data = fob.read()

    print(data)
