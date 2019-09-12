#!/usr/bin/python3
if __name__ == "__main__":    
    import sys
    args = sys.argv
    len_args = len(args) - 1
    i = 1
    j = 1
    if len_args == 0:
        print("{:d} arguments.".format(len_args))
    elif len_args == 1:
        print("{:d} argument:".format(len_args))
        print("{:d}: {:s}".format(i, args[1]))
    else:
        print("{:d} arguments:".format(len_args))
        for j in args[1:]:
            print("{:d}: {:s}".format(i, j))
            i += 1
