#!/usr/bin/python3
'''
-----------------------
Python script that fetches https://intranet.hbtn.io/status
-----------------------
'''
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        body = response.read()
        print('\t- type: ' + str(type(body)))
        print('\t- content: ' + str(body))
        print('\t- utf8 content: ' + str(body.decode('utf-8')))
