print("Enter an operator (+, -, *, /)")

choice = input("Enter your choice: ")

if choice in ('+', '-', '*', '/'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"{num1} + {num2} = {num1 + num2}")

    if choice == '-':
        print(f"{num1} - {num2} = {num1 - num2}")

    if choice == '*':
        print(f"{num1} * {num2} = {num1 * num2}")

    if choice == '/':
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid input")
