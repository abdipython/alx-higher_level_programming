#!/usr/bin/python3
"""fetch intrabet.hbnb.io/status with req"""
from requests import get


if __name__ == '__main__':
    url = get('https://intranet.hbnb.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.content.decode('utf-8')))
