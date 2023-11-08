#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = new_matrix(map(lambda x: x**2, range(len(matrix))))
    return(new_matrix)
