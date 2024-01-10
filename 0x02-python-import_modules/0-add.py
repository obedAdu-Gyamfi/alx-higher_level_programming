#!/usr/bin/python3
# ----------------------------------
# This module imports the add_0 module

# The add_0 function adds two numbers
# -----------------------------------

from add_0 import add

a = 1
b = 2

if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
