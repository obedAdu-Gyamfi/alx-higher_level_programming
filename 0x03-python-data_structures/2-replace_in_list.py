#!/usr/bin/python3

# ------------------------
# This Python function replaces an element of a
# list at a specific index position
# @Obed Adu-Gyamfi
# ------------------------------------

def replace_in_list(my_list, idx, element):

    """ If idx is negetive, this function does not modify anything,
        and returns the original list
        If idx is out of range, or number of elements in my_list,
        this function does not modify anything, and returns the
        orinal function
        Else it returns a modified list at idx.
    """

    if (idx < 0):
        return (my_list)
    elif (idx >= len(my_list)):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
