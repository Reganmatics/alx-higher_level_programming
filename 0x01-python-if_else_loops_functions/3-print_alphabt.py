#!/usr/bin/python3
e_ord = ord('e')
q_ord = ord('q')
for i in range(ord('a'), ord('z')):
    if i != e_ord and i != q_ord:
        print("{:c}".format(i), end="")
