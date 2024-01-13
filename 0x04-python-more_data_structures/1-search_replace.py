#!/usr/bin/python3

# - This is a python function that replaces all occurences
# of an element by anoter in a new list.

def search_replace(my_list, search, replace):
    new_list = []

    for i in range(len(my_list)):
        new_list.append(my_list[i])
        if my_list[i] == search:
            new_list[i] = replace

    return (new_list)
