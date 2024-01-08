#!/usr/bin/python

# -------------------------------
# This function removes the character c from
# Every string.
# @Obed Adu-Gyamfi
# -------------------------------

def no_c(my_string):

    """ Removes the character c from string.

    """
    new_string = []
    for i in my_string:
        new_string.append(i)

    for j in new_string:
        if (j == 'c' or j == 'C'):
            new_string.remove(j)
    r_value = ''.join(new_string)
    return (r_value)
