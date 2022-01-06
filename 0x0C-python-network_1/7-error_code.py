#!/usr/bin/python3
'''This module handles errors for requests'''


if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])

    status = req.status_code

    if status >= 400:
        print('Error code: {}'.format(status))

    else:
        print(req.text)
