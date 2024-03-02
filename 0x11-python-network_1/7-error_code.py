#!/usr/bin/python3
"""
Sends a request to the URL and
displays the statuscode of the body of the 
response (decoded in utf-8)
with `requests` module.
"""
import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
