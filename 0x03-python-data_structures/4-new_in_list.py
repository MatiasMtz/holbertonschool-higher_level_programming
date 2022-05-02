#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        my_listcpy = my_list
        return(my_listcpy)
    my_listcpy = my_list[:]
    my_listcpy[idx] = element
    return my_listcpy
