#!/usr/bin/python3

# ---------------
# Basic python calculator
from add_0 import add

a = 1
b = 2
if __name__ == "__main__":
    """ code would not execute if import with * or __import__"""

    # a = 1
    # b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
