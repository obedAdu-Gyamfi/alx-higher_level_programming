#!/usr/bin/python3

# -----------------------------
# This function insert an element into
# a list at a specific index position
# @Obed Adu-Gyamfi
# ------------------------------

def new_in_list(my_list, idx, element):

    """ If idx is negetive, the function returns a copy
        of the original list.
        If idx is out of range, the function returns a copy
        of the original list.
        Else the function inserts a new element at index postion idx
        into the list forming a new list
    """
    new_list = []
    for i in my_list:
        new_list.append(i)

    if (idx < 0):
        return (my_list)
    elif (idx >= len(my_list)):
        return (my_list)
    else:
        new_list[idx] = element
        return (new_list)
