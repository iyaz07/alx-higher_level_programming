#!/usr/bin/python3
"""Fetches a URL
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}\n\t- utf8 content: {body.decode('utf-8')}")
