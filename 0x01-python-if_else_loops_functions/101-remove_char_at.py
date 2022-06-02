#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for char in str:
        if (j != n):
            string = string + char
        j = j + 1
    return(string)
