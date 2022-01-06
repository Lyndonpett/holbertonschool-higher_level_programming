#!/usr/bin/python3
'''This module sends a POST with a letter as a parameter'''


if __name__ == '__main__':
    import requests
    import sys

    dic = {}

    if len(sys.argv) >= 2:
        dic['q'] = sys.argv[1]

    else:
        dic['q'] = ""

    req = requests.post('http://0.0.0.0:5000/search_user', data=dic)

    try:
        jsonResp = req.json()

        if jsonResp == {}:
            print('No result')

        else:
            print('[{}] {}'.format(jsonResp['id'], jsonResp['name']))

    except Exception:
        print('Not a valid JSON')
