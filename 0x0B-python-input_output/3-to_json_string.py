#!/usr/bin/python3
"""This module returns a JSON rep of an object(string)"""


import json


def to_json_string(my_obj):
    """Returns JSON representation"""

    return json.dumps(my_obj)
