"""
Problem statement:
    A program in python to print fibonacci series using recursive method.
"""

# Assume input and  output
# input: 3
# output: 0 1 1 2 3


# implementation the solution
# ==========================================================

# Generating fibonacci series


def recursive_fibanacci(i):
    if i <= 1:
        return i
    else:
        return recursive_fibanacci(i - 1) + recursive_fibanacci(i - 2)


num = int(input("Enter a number to form fabonacci series: "))

if num <= 0:
    print("Number cannot be negative number or zero")
else:
    print("Fibanacci series: ")
    for i in range(num):
        print(recursive_fibanacci(i), " ", end="")
