#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    totalSum = 0

    for item in my_list:
        if item not in unique_list:
            unique_list.add(item)
            totalSum += item
    return (totalSum)
