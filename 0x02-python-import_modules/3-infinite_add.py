#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]

    total = 0
    for arg in arguments:
        total += int(arg)
    print("{:d}".format(total))
