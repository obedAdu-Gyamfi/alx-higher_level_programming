#!/usr/bin/python3

# -----------------------------
# Function finds all the multiples of 2 in a
# list
# @Obed Adu-Gyamfi
# ------------------------------

def divisible_by_2(my_list=[]):
    """Finds multiples of 2

    Args:
        my_list

    Returns:
        new_list with True of False
    """

    if len(my_list) == 0:
        return (None)

    else:
        new_list = []
        for i in my_list:
            if ((i % 2) == 0):
                new_list.append(True)
            else:
                new_list.append(False)

    return (new_list)
