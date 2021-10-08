#!/usr/bin/python3
"""This module prints 2 newlines after . ? and :"""


def text_indentation(text):
    """Prints newlines after . ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and flag == 1:
            continue

        if i == '.' or i == '?' or i == ':':
            print("{}{}".format(i, '\n'))
            flag = 1

        else:
            print(i, end="")
            flag = 0
