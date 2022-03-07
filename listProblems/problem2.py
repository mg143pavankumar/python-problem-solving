# Python program to swap two elements in a list

"""
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
"""

# solution

# method-1


def swap_two_element_by_pos(myList, pos1, pos2):
    myList[pos1], myList[pos2] = myList[pos2], myList[pos1]

    return myList

# method-2


def swap_element(newList, pos1, pos2):

    # pop the elements
    first_element = newList.pop(pos1)
    second_element = newList.pop(pos2-1)

    # insert the element
    newList.insert(pos1, second_element)
    newList.insert(pos2, first_element)

    return newList


myList = [23, 65, 19, 90]

pos1, pos2 = 1, 3

# print(swap_two_element_by_pos(myList, pos1 - 1, pos2 - 1))
print(swap_element(myList, pos1 - 1, pos2 - 1))
