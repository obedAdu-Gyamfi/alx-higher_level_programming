#!/usr/bin/python3

def print_last_digit(number):
    value = int(repr(number)[-1])
    print("{}".format(value), end="")
    return (value)
