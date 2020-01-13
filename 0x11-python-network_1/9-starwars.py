#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import requests
import sys

if __name__ == "__main__":
    try:
        request = requests.get(
                'https://swapi.co/api/people/?search=' + sys.argv[1])
        null = None
        dic = eval(request.text)

        if len(dic) > 0:
            print('Number of results: {}'.format(dic['count']))
            for result in dic['results']:
                print(result['name'])
        else:
            print('No result')
    except Exception as e:
        print('Not a valid JSON')
