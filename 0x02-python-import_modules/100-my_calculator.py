#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    alist = []
    for line in argv[1:]:
        alist.append(line)

    if (len(alist) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    if (operator == "+"):
        a = int(alist[0])
        b = int(alist[2])
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (operator == "*"):
        a = int(alist[0])
        b = int(alist[2])
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (operator == "-"):
        a = int(alist[0])
        b = int(alist[2])
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (operator == "/"):
        a = int(alist[0])
        b = int(alist[2])
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
