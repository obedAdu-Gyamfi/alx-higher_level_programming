#!/usr/bin/python3

# -------------------------
# Function deletes  an item at a specific
# index position idx
# @Obed Adu-Gyamfi
# ----------------------------

def delete_at(my_list=[], idx=0):
    """ If idx is negetive or out of range, nothing changes.

    Args:
        my_list
        idx

    Returns:
        new_list
    """

    if (idx < 0):
        return (my_list)
    elif (idx >= len(my_list)):
        return (my_list)
    else:
        del my_list[idx]

    return (my_list)
