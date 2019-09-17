#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for element in matrix:
        if (len(element)-1)<0:
            continue
        for i in range(len(element)-1):
            print("{:d}".format(element[i]), end=" ")
        
        print("{:d}".format(element[(len(element)-1)]))
