#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_order = list(a_dictionary.list_order())
    for i in list_order:
        for i in sorted(a_dictionary):
            print("{}: {}".format(i, a_dictionary[i]))
