#!/usr/bin/python3
"""This fetchs the status of https://alx-intranet.hbnb.io/status"""
from urllib import request

if __name__ == "__main__":
    '''url http service'''
    url = 'https://intranet.hbnb.io/status'

    with request.urlopen(url) as response:
        html_body = response.read()
        print('Body response:')
        print('\t- typr: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
