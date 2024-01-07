#!/usr/bin/python3

# --------------------
# This is a python function that
# prints all integers in a reversed order
# @Obed Adu-Gyamfi
# ---------------------------

def print_reversed_list_integer(my_list=[]):

    """ Function prints a list of integers in
        reversed form
    """
    for i in my_list:
        print("{:d}".format(my_list[-i]))
