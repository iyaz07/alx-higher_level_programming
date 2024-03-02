#!/usr/bin/python3
"""Script to send a POST request to a URL with email parameter"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
