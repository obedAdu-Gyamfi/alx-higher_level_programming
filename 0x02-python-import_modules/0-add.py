#!/usr/bin/python3
# ----------------------------------
# This module imports the add_0 module

# The add_0 function adds two numbers
# -----------------------------------

if __name__ == "__main__":
    """ code would not execute if import with * or __import__"""
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
