#!/usr/bin/python3

# - This is a python function that replaces all occurences
# of an element by anoter in a new list.

def search_replace(my_list, search, replace):

    for i in range(len(my_list) - 1):
        if my_list[i] == search:
            my_list[i] = replace

    return (my_list)
