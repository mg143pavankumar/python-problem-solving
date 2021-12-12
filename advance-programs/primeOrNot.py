"""
Problem-statment:
    Write a program to check given number is prime or not?
"""

# Assume input and output
# input: 5
# output: prime

# input: 4
# output: not prime


# Come up with correct solution for the problem. State it in plain English
'''
    1. Take user input as int type
    2. create a variable flag = 1
    3. check weather it prime or not
    4. if it is prime number than display "prime number"
    5. if not display "Not a prime number"
'''

# implementation the solution
# ==========================================================


# Function for checking condition

def checkPrimeOrNot(num):
    flag = False
    # checking weather given number is prime or not
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        return flag


def displayOutput(num):
    result = checkPrimeOrNot(num)
    print(result)

    if result:
        print(num, " is not a prime number")
    else:
        print(num, " is a prime number")


# Take the user input as int type
num = int(input("Enter a number to know weather it is prime or not:  "))

# Calling function
displayOutput(num)
