# Python Program to Swap Two Variables


# swaping by using third variable
def swap_two_numbers_by_third_variable(num1, num2):
    print(f"Before swapping \nnum1 = {num1} \nnum2 = {num2}")

    temp = num1
    num1 = num2
    num2 = temp

    print(f"After swapping\nnum1 = {num1} \nnum2 = {num2}")


# swaping without using third vairable
def swapTwoNumbers(num1, num2):

    print(f"Before swapping \nnum1 = {num1} \nnum2 = {num2}")

    num1, num2 = num2, num1

    print(f"After swapping \nnum1 = {num1} \nnum2 ={num2}")


# calling functions
swap_two_numbers_by_third_variable(2, 4)
swapTwoNumbers(2, 4)
