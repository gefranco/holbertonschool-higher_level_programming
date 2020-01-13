#!/usr/bin/python3
'''
-----------------------
Python script that displays the X-Request-Id variable in the header.
-----------------------
'''
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
