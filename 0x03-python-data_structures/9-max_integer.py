#!/usr/bin/python3
# ------------
# prints  the biggest integer of a list.
# @Obed Adu-Gyamfi
# ----------------

def max_integer(my_list=[]):

    """
        Prints the maximum integer of a list

    Args:
        my_list
    """
    max_int = 0

    if len(my_list) == 0:
        return (None)
    else:
        for i in my_list:
            if (i > max_int):
                max_int = i

    return (max_int)
