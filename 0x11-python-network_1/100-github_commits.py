#!/usr/bin/python3
"""get repo 10 commits"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url, params={'per_page': 10})
    for commit in res.json():
        name = commit['commit']['author']['name']
        print("{}: {}".format(commit['sha'], name))
