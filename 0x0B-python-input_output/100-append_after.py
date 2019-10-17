#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        lines = myFile.readlines()
        count = 0

    with open(filename, mode="w", encoding="utf-8") as myFile:
        for line in lines:
            myFile.write(line)
            if search_string in line:
                myFile.write(new_string)
