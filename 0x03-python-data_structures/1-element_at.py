#!/usr/bin/python3
__author__ = "Reganmatics"


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
