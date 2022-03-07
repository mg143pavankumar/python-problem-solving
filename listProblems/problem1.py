# Python program to interchange first and last elements in a list
"""
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
"""

# Solution


# method-1
def swap_list_by_third_var(newList):
    """Swaping first element with last element using third variable"""
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp

    return newList


# method-2
def swap_list_without_third_var(newList):
    """Swapping first and last element without using third variable"""

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList


# method-3
def swap_list_using_astrik_sym(newList):
    """Swapping list using using * symbulls"""

    start, *middle, end = newList
    newList = [end, *middle, start]

    return newList


# method-4
def swap_list_using_tuple_var(list):
    """Swapping list using tuple variable"""

    get = list[-1], list[0]
    list[0], list[-1] = get

    return list


# let list be
myList = [12, 35, 9, 56, 24]

# print(f"Swapped list: {swap_list_by_third_var(myList)}")
# print(f"Swapped list: {swap_list_without_third_var(myList)}")
# print(f"Swapped list: {swap_list_using_astrik_sym(myList)}")
print(f"Swapped list: {swap_list_using_tuple_var(myList)}")
