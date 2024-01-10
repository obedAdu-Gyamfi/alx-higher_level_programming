#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    """ Code does not execute if imported with * or __import__
    """

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
