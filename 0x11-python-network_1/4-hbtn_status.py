#!/usr/bin/python3
'''
-----------------------
Python script that fetches https://intranet.hbtn.io/status
-----------------------
'''
import requests

if __name__ == "__main__":
    print("Body response:")
    request = requests.get('https://intranet.hbtn.io/status')
    print('\t- type: ' + str(type(request.text)))
    print('\t- content: ' + request.text)
