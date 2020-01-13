#!/usr/bin/python3
'''
-----------------------
Python script that sends a POST request and displays the the body.
-----------------------
'''
import requests
import sys

if __name__ == "__main__":
    data = {}
    data['q'] = ''
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    try:
        request = requests.post('http://0.0.0.0:5000/search_user', data=data)
        dic = eval(request.text)
        if len(dic) > 0:
            print('[{}] {}'.format(dic['id'], dic['name']))
        else:
            print('No result')
    except Exception as e:
        pass
