#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    len_args = len(args) - 1

    if len_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if args[2] != "+" and args[2] != "-" and args[2] != "*" and args[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif args[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif args[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
