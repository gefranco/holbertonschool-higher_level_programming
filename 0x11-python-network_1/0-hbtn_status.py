#!/usr/bin/python3
'''
-----------------------
Python script that fetches https://intranet.hbtn.io/status
-----------------------
'''
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print("Body Response:")
    for line in response:
        print('\t- type: ' + str(type(line)))
        print('\t- content: ' + str(line))
        print('\t- utf8 content: ' + str(line.decode('utf-8')))
