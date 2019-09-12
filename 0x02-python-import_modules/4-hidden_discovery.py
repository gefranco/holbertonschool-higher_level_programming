#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    args = dir(hidden_4)
    len_args = len(args)
    i = 1
    arg = ""
    for j in args:
        arg = j
        if j[0:2] == "__":
            continue
        print("{:s}".format(j))
