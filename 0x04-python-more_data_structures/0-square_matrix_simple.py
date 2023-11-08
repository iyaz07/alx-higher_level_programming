#!/usr/bin/python3
def square_matrix_simple(matrix):
    row_num = len(matrix)
    col_num = len(matrix[0])

    new_matrix = [[0] * col_num for _ in range(row_num)]

    for i in range(row_num):
        for j in range(col_num):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)
