#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    new_list = set(my_list)
    for i in new_list:
        sum_list += i
    return sum_list
