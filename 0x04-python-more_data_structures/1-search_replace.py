#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = [replace if i == search else i for i in my_list]
    return new_matrix
