#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")

"""
def pal(num: int) -> int:
    rev = int(str(num)[::-1])
    return rev

for i in range(100):
    if i != 89:
        if i == max(i, pal(i)) and (i == pal(i)):
            continue
        if i == min(i, pal(i)):
            print("{:02d}".format(i), end=", ")
        if i == 89:
            print("{:02d}".format(i))
print(pal(12487))
"""
