#!/usr/bin/python3
"""
function that appends a string at the end of a text
"""

def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)
