#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        if i % 2:
            result = result + [False]
        else:
            result = result + [True]
    return result
