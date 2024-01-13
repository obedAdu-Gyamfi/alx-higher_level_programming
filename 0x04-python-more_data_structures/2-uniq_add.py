#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum_value = 0
    for i in uniq:
        sum_value += i

    return(sum_value)
