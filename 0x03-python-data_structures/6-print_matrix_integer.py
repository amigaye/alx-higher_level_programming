#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
