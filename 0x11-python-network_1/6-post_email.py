#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import requests
import sys

if __name__ == "__main__":
    values = {}
    values['email'] = sys.argv[2]

    request = requests.post(sys.argv[1], data=values)
    print(request.text)
