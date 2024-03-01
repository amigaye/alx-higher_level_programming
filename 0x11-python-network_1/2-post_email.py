#!/usr/bin/python3
"""
This script takes in a URL and an email
"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    result = urllib.parse.urlencode(mail).encode("ascii")
    request = urllib.request.Request(url, result)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
