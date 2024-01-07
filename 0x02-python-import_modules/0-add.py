#!/usr/bin/python3
# ----------------------------------
# This module imports the add_0 module

# The add_0 function adds two numbers
# -----------------------------------

import add_0

a = 1
b = 2

if __name__ == "__main__":
    """ This module would not be imported if
        __import__ or __import__ * is used to
        import
    """
    print(f"{a} + {b} = {add_0.add(a, b)}")
