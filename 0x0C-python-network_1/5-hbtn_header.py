#!/usr/bin/python3
'''This module displays X-Requests-Id'''


if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])

    data = req.headers

    print(data.get('X-Request-Id'))
