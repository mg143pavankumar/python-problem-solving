"""
    Write a program to count number of words in camelCaseString
    Ex: helloWorld   # o/p 2
"""


def no_of_words(newString):
    count = 0
    arr = []

    if newString == "":
        count = - 1
    else:
        [[arr.append(i) for i in newString if i.isupper()]]
        count = len(arr)

    return count + 1


myString = "helloWorldHowAreYouDoing"
print(no_of_words(myString))
