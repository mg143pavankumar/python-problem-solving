'''
Problem Statement:
    Program in python to check whether a number is palindrome or not by recusive method.
'''

# Algorithm for the solution
'''
    1. Take the input from user and store it in a variable
    2. Store the value in a temp variable
    3. Using while loop, get all the digit of a number and store the reverse number in another varaible
    4. if temp value is equal to reverse number than display "It is palindrome number" else "not a palindrome number"
'''

# Implementation for the solution

rev = 0


def recursive_reverseNumber(n):
    global rev
    if n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        recursive_reverseNumber(int(n / 10))
    return rev


n = int(input("Enter a number:"))

rev_num = recursive_reverseNumber(n)
if rev_num == n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome:")
