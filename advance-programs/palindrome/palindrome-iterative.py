'''
Problem Statement:
    Program in python to check whether a number is palindrome or not.
'''

# Algorithm for the solution
'''
    1. Take the input from user and store it in a variable
    2. Store the value in a temp variable
    3. Using while loop, get all the digit of a number and store the reverse number in another varaible
    4. if temp value is equal to reverse number than display "It is palindrome number" else "not a palindrome number"
'''

# Implementation for the solution

# Taking input from the user
num = int(input("Enter a number to check for palindrome: "))
rev = 0

# function for generating reverse of a number


def reverseNumber(num):
    global rev

    # Here we are reversing the original value
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev


# getting the reverse number and storing in a variable
rev_num = reverseNumber(num)

if rev_num == num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")
