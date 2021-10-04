#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    for x in newDic:
        newDic[x] *= 2

    return newDic
