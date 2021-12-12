'''
probelm statement:
    program in python to find the sum of digit of a number using recursive method
'''

# function for calculating sum of digits


def recursive_getSumOfNumber(num):

    if num == 0:
        return num

    return (num % 10 + recursive_getSumOfNumber(num // 10))


# Taking input from the user
num = int(input("Enter a number: "))

# Display the output
print(f"Sum of digit of {num}:=> {recursive_getSumOfNumber(num)}")
