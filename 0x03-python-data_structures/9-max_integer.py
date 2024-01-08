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

    if len(my_list) == 0:
        return (None)
    else:
        max_int = my_list[0]
        for i in my_list:
            if (i > max_int):
                max_int = i

    return (max_int)
