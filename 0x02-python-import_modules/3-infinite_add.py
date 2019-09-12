#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    len_args = len(args) - 1
    i = 1
    num = 0
    for j in args[1:]:
        num = num + int(j)

    print("{:d}".format(num))
