#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    uniq_sum = 0
    for i in range(len(my_list)):
        if (my_list[i] not in new_list):
            new_list.append(my_list[i])
            uniq_sum += my_list[i]
    return (uniq_sum)
