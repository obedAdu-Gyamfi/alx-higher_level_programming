#!/usr/bin/python3
# --------------------------------
# This is a function that adds two
# tuples
# @Obed Adu-Gyamfi
# --------------------------------
def add_tuple(tuple_a=(), tuple_b=()):

    """ This function adds two tuples

    Args:
        tuple_a: tuple a
        tuple_b: tuple b

    Return:
        new_tuple: added tuple
    """
    if (len(tuple_a) < 2):
        filled_a = tuple_a + (0, ) * (len(tuple_b) - len(tuple_a))
        new_tuple = tuple(x + y for x, y in zip(filled_a, tuple_b))
    elif (len(tuple_b) < 2):
        filled_b = tuple_b + (0, ) * (len(tuple_a) - len(tuple_b))
        new_tuple = tuple(i + j for i, j in zip(tuple_a, filled_b))
    elif (len(tuple_a) > 2):
        shrt_a = tuple_a[:2]
        new_tuple = tuple(i + j for i, j in zip(shrt_a, tuple_b))
    elif (len(tuple_b) > 2):
        shrt_b = tuple_b[:2]
        new_tuple = tuple(a + b for a, b in zip(tuple_a, shrt_b))
    else:
        new_tuple = tuple(x + y for x, y in zip(tuple_a, tuple_b))

    return (new_tuple)
