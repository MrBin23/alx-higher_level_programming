#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for my_row in range(len(matrix)):
            for my_item in range(len(matrix[my_row])):
                if my_item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[my_row][my_item]), end=endspace)
            print()
