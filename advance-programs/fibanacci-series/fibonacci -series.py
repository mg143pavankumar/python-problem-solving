"""
Problem statement:
    A program in python to print fibonacci series using iterative method.
"""

# Assume input and  output
# input: 3
# output: 0 1 1 2 3

# Come up with correct solution. State it in plain english
'''
    1. Take the user input and store in num variable
    2. let n1 = 0, n2 = 1 and  count = 0
    3. if num <= 0 then display "0 or negative are not allowed"
    4. if num == 1 then display n1 value else
    5. generate fabonacci series from 0 to num

'''

# implementation the solution
# ==========================================================

# Generating fibonacci series


def generateFibonacciSeries(num, count):
    n1, n2 = 0, 1

    if num <= 0:
        print("Negative and zero values are not allowed")
    elif num == 1:
        print(f"Fibonacci series of {num} is : {n1}")
    else:
        while count < num:
            print(n1, " ", end="")
            nth = n1 + n2

            # update values
            n1 = n2
            n2 = nth
            count += 1


# Taking input from the user
num = int(input("Enter a number to form fabonacci series: "))

count = 0
generateFibonacciSeries(num, count)
