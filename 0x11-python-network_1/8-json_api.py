#!/usr/bin/python3
"""
This script takes in a letter and sends
"""
import requests
import sys


if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    query = {"q": letter}
    request = requests.post("http://0.0.0.0:5000/search_user", query)

    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
