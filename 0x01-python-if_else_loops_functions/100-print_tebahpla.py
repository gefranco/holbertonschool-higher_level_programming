#!/usr/bin/python3
letter = 122
while letter >= ord('a'):

    if(letter % 2 == 0):
        print("{:c}".format(letter), end="")
    else:
        print("{:c}".format(letter - 32), end="")
    letter -= 1
