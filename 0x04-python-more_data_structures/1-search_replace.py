#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for element in range(len(my_list)):
        if my_list[element] == search:
            result.append(replace)
        else:
            result.append(my_list[element])
            return result
