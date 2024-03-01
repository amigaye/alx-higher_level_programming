#!/usr/bin/python3
"""
This script takes in a URL and an email address
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    request = requests.post(url, mail)
    print(request.text)
