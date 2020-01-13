#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    try:
        request = requests.get(
                'https://api.github.com/user',
                auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))

        false = False
        null = None
        dic = eval(request.text)

        print('{}'.format(dic['id']))
    except Exception as e:
        print('None')
