num = int(input("Enter a number: "))

# let
factorial = 1

if num < 0:
    print("factorial of ", num, " doesn't exist")
elif num == 0:
    print("Factorial of ", num, " is ", factorial)
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of ", num, " is ", factorial)
