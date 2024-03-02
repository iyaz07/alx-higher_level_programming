#!/usr/bin/python3
"""This is a description"""
import requests
import sys

if __name__ == "__main__":
    Repo = sys.argv[1]
    Owner = sys.argv[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(Owner, Repo)
    req = requests.get(URL)

    if req.status_code == 200:
        Commit_list = req.json()
        for commit in Commit_list[:10]:
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(commit['sha'], author_name))
