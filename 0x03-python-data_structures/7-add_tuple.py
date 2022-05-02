#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_A = tuple_a + (0, 0)
    tuple_B = tuple_b + (0, 0)
    new_tuple = tuple_A[0] + tuple_B[0], tuple_A[1] + tuple_B[1]
    return new_tuple
