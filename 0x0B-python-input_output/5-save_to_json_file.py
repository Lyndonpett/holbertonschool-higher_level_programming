#!/usr/bin/python3
"""This module writes an Object to a text file, using a JSON rep"""


import json


def save_to_json_file(my_obj, filename):
    """Text file to JSON REP"""

    with open(filename, "w") as outfile:
        outfile.write(json.dumps(my_obj))
