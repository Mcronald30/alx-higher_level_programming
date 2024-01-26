#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_object = response.json()
        for x, obj_ in enumerate(json_object):
            if x == 10:
                break
            if type(obj) is dict:
                name = obj_.get('commit').get('author').get('name')
                print("{}: {}".format(obj_.get('sha'), name))
    except ValueError as invalid_json:
        pass
