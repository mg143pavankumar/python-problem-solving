# Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

from mimetypes import guess_type


def findLeapYear(given_year):

    no_of_next_years = 15
    list_of_leap_years = []

    for i in range(given_year, given_year + 1 + no_of_next_years * 4):

        # num divisible by 400 --- leap year and divisible by 100 --- centery year
        if((i % 400 == 0) and i % 100 == 0):
            list_of_leap_years.append(i)

        # num divisible by 4 and not divisible by 100 --- leap year
        if (i % 4 == 0 and i % 100 != 0):
            list_of_leap_years.append(i)
    return list_of_leap_years


list_of_leap_years = findLeapYear(2000)
print(list_of_leap_years)
