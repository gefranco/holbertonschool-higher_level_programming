#!/usr/bin/python3
'''
-----------------------
Python script that displays the X-Request-Id variable in the header.
-----------------------
'''
import requests
import sys

if __name__ == "__main__":
    try:
        request = requests.get(sys.argv[1])
        print(request.headers['X-Request-Id'])
    except:
        pass
