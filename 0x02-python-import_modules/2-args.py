#!/usr/bin/python3
import sys

if (len(sys.argv) < 2):
    print("0 arguments.")
else:
    if (len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
