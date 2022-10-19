#!/usr/bin/python3

"""
this script writes to a test file
"""


def write_file(filename="", text=""):
    """
    args:
        filename -> file path
        text -> text to write to filename
    """
    with open(filename, mode="w", encoding="UTF8") as fob:
        fob.write(text)
        return len(text)
