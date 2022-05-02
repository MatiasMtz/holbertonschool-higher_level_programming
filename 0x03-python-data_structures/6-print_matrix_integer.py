#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for number in i:
            print(f"{number}", end="")
            if number != i[-1]:
                print(f" ", end="")
        print()
