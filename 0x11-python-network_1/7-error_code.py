#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import requests
import sys

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code > 400:
        print('Error code: ' + str(request.status_code))
    else:
        print(request.text)
