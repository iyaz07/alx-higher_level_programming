#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
Except HTTPError exceptions, 
print the HTTP Status Code.
"""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            s = url.read()
            print(s.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
