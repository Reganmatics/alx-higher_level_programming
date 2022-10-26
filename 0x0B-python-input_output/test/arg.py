#!/usr/bin/python3
"""
this script tests the usecase of the command line arguments
"""
import sys


def get_args():
    """
    args:
        ar -> argument vector
    """

    result = ''
    for i in range(len(sys.argv)):
        result += f'arg{i} = {sys.argv[i]}\n'
    return result

def main():
    print(get_args())


if __name__ == "__main__":
    main()
