#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        lines = myFile.readlines()
        count = 0
        for line in lines:
            print(line, end="")
            count += 1

            if count == nb_lines:
                break
