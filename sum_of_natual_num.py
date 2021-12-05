num = int(input("Enter a number: "))

# for finding sum of natural number
if num < 0:
    print("Please enter only positive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("Sum of natrual number is : ", sum)
