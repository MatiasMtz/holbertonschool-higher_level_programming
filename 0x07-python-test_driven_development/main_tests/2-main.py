#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1.000, 2.000, 3.000]
]
div = (1, )
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, div))
