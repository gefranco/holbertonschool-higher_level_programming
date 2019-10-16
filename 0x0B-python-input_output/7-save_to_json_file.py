#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):

    with open(filename, mode="w", encoding="utf-8") as myFile:
        json_obj = json.dumps(my_obj)
        myFile.write(json_obj)
