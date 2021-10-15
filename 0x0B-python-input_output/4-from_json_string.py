#!/usr/bin/python3
"""This module returns an object rep by a JSON string"""

import json


def from_json_string(my_str):
    """Takes an object and returns the JSON string"""

    return json.loads(my_str)
