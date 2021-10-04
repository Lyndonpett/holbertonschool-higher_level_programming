#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for x in range(len(my_list)):
        if newList[x] == search:
            newList[x] = replace

    return (newList)
