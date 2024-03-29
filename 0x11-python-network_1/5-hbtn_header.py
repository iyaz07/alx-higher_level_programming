#!/usr/bin/python3
"""
Sends a request to a URL to -
display the value of the `X-Request-Id`
variable found in the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    print("{}".format(requests.get(sys.argv[1]).headers.get('X-Request-Id')))
