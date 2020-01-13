#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import urllib.request
import urllib.parse
import sys
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    values = {}
    values['email'] = sys.argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(req) as response:
            for line in response:
                print(str(line.decode('utf-8')))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
