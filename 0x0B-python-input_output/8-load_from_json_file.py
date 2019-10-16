#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename, mode="r", encoding="utf-8") as myFile:
        obj = ""
        json_obj = myFile.read()

        if json_obj != "":
            obj = json.loads(json_obj)

        return obj
