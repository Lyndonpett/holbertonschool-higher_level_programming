#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newDic = a_dictionary.copy()
    for x in sorted(newDic):
        print("{}: {}".format(x, newDic[x]))
