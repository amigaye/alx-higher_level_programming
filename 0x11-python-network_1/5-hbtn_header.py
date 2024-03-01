#!/usr/bin/python3
"""
This script takes in a URL, sends a request
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))
