#!/usr/bin/python3
'''This module posts an email with Python'''


if __name__ == '__main__':
    import sys
    from urllib import request, parse

    dic = {}

    dic['email'] = sys.argv[2]

    data = parse.urlencode(dic)

    dic = data.encode('UTF-8')

    req = request.Request(sys.argv[1], dic)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('UTF-8'))
