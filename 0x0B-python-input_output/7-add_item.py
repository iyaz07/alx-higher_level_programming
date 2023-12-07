#!/usr/bin/python3
"""
This script demonstrates json adding all arguments to
a Python list, and then save them to a file.
"""


import json
import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    The main function
    """
    path = Path("add_item.json")
    if path.is_file():
        jslist = load_from_json_file("add_item.json")
    else:
        jslist = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            jslist.append(sys.argv[i])
    save_to_json_file(jslist, "add_item.json")


main()
