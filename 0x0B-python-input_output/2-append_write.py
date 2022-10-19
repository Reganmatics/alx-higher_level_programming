#!/usr/bin/python3
"""
task: append string to the end of a text file and return number of characters
"""


def append_write(filename="", text="", encoding="UTF8"):
    """
    args:
        filename -> path to file
        text -> string to append to end of file
    """
    with open(filename, mode="a") as fob:
        fob.write(text)
    return len(text)
