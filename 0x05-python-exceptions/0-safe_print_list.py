#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        a = ""
        for i in range(x):
            a += str(my_list[i])
        return (int(a))
    except IndexError:
        return (int(my_list[-1]))


if __name__ == "__main__":
    safe_print_list()
