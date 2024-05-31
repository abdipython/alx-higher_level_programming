#!/usr/bin/python3
"""sends a PO request to the passed URL with the email as par"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
