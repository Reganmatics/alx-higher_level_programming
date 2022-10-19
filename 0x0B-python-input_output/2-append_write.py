#!/usr/bin/python3
"""
task: append string to the end of a text file and return number of characters
"""


def append_write(filename="", text=""):
    with open(filename, mode="a") as fob:
        fob.write(text)
    return len(text)
