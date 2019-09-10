#!/usr/bin/python3
i = 0
j = 0
while i < 9:
    j = i + 1
    while j <= 9:
        if j == 9 and i == 8:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d},".format(i, j), end=" ")
        j += 1
    i += 1
