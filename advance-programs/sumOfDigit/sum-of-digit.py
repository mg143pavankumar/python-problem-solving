'''
probelm statement:
    program in python to find the sum of digit of a number
'''

# function for calculating sum of digits


def getSumOfNumber(num):
    sum = 0

    for digit in str(num):
        sum += int(digit)
    return sum


# Taking input from the user
num = int(input("Enter a number: "))

# Display the output
print(f"Sum of digit of {num}:=> {getSumOfNumber(num)}")
