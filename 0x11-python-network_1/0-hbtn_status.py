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
        print('    - type: ' + str(type(line)))
        print('    - content: ' + str(line))
        print('    - utf8 content: ' + str(line.decode('utf-8')))
