#!/usr/bin/python3
"""
error code
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response = response.read().decode("utf-8")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
