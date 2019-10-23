#!/usr/bin/python3
'''
=============
module for the Base class
============
'''

import json
import os


class Base:
    '''class Base. assign an id to every object created'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init method'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        strjson = json.dumps(list_dictionaries)
        return strjson

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is None:
            list_objs = []
        dictionary_list = []
        for li in list_objs:
            dictionary_list.append(li.to_dictionary())

        strjson = Base.to_json_string(dictionary_list)

        with open(cls.__name__+".json", mode="w", encoding="utf-8") as file:

            file.write(strjson)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if dictionary is None:
            return None
        if cls.__name__ is "Rectangle":
            r1 = cls(10, 10)
        else:
            r1 = cls(10)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances from a file'''

        if not os.path.isfile(cls.__name__ + ".json"):
            return []

        with open(cls.__name__+".json", mode="r", encoding="utf-8") as f:
            strjson = f.read()

        list_dictionaries = Base.from_json_string(strjson)

        list_obj = []
        for i in list_dictionaries:
            list_obj.append(cls.create(**i))

        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):

        with open(cls.__name__+".csv", mode="w", encoding="utf-8")as f:
            for i in list_objs:
                row = ""
                dic = i.to_dictionary()
                if cls.__name__ is "Rectangle":
                    row = str(dic["id"])
                    row += ","+str(dic["width"])
                    row += ","+str(dic["height"])
                    row += ","+str(dic["x"])
                    row += ","+str(dic["y"])+"\n"
                else:
                    row = str(dic["id"])
                    row += ","+str(dic["size"])
                    row += ","+str(dic["x"])
                    row += ","+str(dic["y"])+"\n"
                f.write(row)

    @classmethod
    def load_from_file_csv(cls):
        list_obj = []
        with open(cls.__name__+".csv", mode="r", encoding="utf-8")as f:
            rows = f.readlines()

        for row in rows:
            columns = row.split(",")
            dict_o = {}
            if cls.__name__ is "Rectangle":
                dict_o["id"] = int(columns[0])
                dict_o["width"] = int(columns[1])
                dict_o["height"] = int(columns[2])
                dict_o["x"] = int(columns[3])
                dict_o["y"] = int(columns[4])
            else:
                dict_o["id"] = int(columns[0])
                dict_o["size"] = int(columns[1])
                dict_o["x"] = int(columns[2])
                dict_o["y"] = int(columns[3])

            list_obj.append(cls.create(**dict_o))
        return list_obj
