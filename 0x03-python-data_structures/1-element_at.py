#!/usr/bin/python3

# ----------------------

# This is a python function that retrieves an
# element from a list like in c.
# ---------------------------

def element_at(my_list, idx):

    """ if idx is negetive, the function returns
        None
        Else if idx is out of range, the function returns
        None
        Else The function returns the element at index position
        idx
    """

    if (idx < 0):
        return (None)

    elif (idx >= len(my_list)):
        return (None)
    else:
        return (my_list[idx])
