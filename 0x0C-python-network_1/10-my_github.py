#!/usr/bin/python3
'''This module uses the GITHUB api'''


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    token = sys.argv[2]
    user = sys.argv[1]
    params = {'state': 'open'}
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=HTTPBasicAuth(user, token), params=params)

    jsonStr = req.json()
    print(jsonStr.get('id'))
