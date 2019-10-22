#!/usr/bin/python3
"""
=============
module base
============
"""

import json
from pathlib import Path


class Base:
    """class Base. main class, assign an id to every object created

    Attributes:
        __nb_objects    the number of objects created

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        strjson = json.dumps(list_dictionaries)
        return strjson

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        dictionary_list = []
        for li in list_objs:
            dictionary_list.append(li.to_dictionary())

        strjson = Base.to_json_string(dictionary_list)

        with open(cls.__name__+".json", mode="w", encoding="utf-8") as file:

            file.write(strjson)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        r1 = cls(10, 10)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances from a file
        """

        fc = Path(cls.__name__+".json")

        if not fc.is_file():
            return []

        with open(cls.__name__+".json", mode="r", encoding="utf-8") as f:
            strjson = f.read()

        list_dictionaries = Base.from_json_string(strjson)

        list_obj = []
        for i in list_dictionaries:
            list_obj.append(cls.create(**i))

        return list_obj
