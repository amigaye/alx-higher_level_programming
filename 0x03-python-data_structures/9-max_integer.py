#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    for i in range(len(my_list)):
        if (max_num < my_list[i]):
            max_num = my_list[i]
        else:
            max_num = max_num
    return (max_num)
