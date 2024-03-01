#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
"""
import urllib.error
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
