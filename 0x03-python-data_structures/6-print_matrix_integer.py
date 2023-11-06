#!usr/bin/pyhton3
def print_matrix_integer(matrix=[[]]):
    rowCount = len(matrix)

    for i in range(rowCount):
        elementCount = len(matrix[i])

        for j in range(elementCount):
            print('{:d}'.format(matrix[i][j]), end='')
            print(end=' ' if j < (elementCount - 1) else '')
        print(end='\n')
