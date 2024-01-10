#!/usr/bin/python3
# -------------------------
# A python basic calculator
# This module does not execute if imported with * or
# __import__
# (c) Obed Adu-Gyamfi
# Email: adugyamfiobed.tpp3@gmail.com
# ------------------------
from calculator_1 import add, sub, mul, div
a = 10
b = 5

if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
