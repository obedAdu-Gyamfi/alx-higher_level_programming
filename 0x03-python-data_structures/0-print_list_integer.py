#!/usr/bin/python3

# This is a module that prints a list
# of integers

def print_list_integer(my_list=[]):

    """ This function prints a list of integers
        The function loops over the lists
        and prints out each member of the list
    """

    for i in my_list:
        print("{:d}".format(i))
