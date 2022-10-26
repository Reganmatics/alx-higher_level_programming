#!/usr/bin/python3
"""
this script adds all arguments to a python list and saves them to a file
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file   = __import__('5-save_to_json_file').save_to_json_file


file = 'add_item.json'
if file in os.listdir():
    pass
else:
    os.system(f'touch {file}')

my_obj = load_from_json_file(file)
my_obj.append(i for i in sys.argv[1:])
save_to_json_file(file)
