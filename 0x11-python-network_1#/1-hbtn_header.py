#!/usr/bin/python3
"""sends a request to the URL that displays the value of X-Req ID"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        val = response.info()

    print(val['X-Request-Id'])
