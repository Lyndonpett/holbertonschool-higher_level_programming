#!/usr/bin/python3
'''This module posts an email with requests.'''


if __name__ == '__main__':
    import requests
    import sys

    dic = {}

    dic['email'] = sys.argv[2]

    req = requests.post(sys.argv[1], dic)

    print(req.text)
