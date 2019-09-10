#!/usr/bin/python3
letter = 97
while letter <= ord('z'):
    if letter == ord('q') or letter == ord('e'):
        letter += 1
        continue
    else:
        print("{:c}".format(letter), end="")
    letter += 1
