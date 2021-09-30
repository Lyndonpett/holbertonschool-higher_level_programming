#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tupA = (0, 0)
    elif len(tuple_a) == 1:
        tupA = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        tupA = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tupB = (0, 0)
    elif len(tuple_b) == 1:
        tupB = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        tupB = (tuple_b[0], tuple_b[1])
    return (tupA[0] + tupB[0], tupA[1] + tupB[1])
