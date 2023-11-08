#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_my_list = my_list.copy()
    for i in range(len(new_my_list)):
        if (new_my_list[i] == search):
            new_my_list[i] = replace
    return (new_my_list)
