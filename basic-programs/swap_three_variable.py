# Swapping using three variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("<------ Before swapping ------->")
print(f"first number: {num1}\nSecond number: {num2}")

# swapping two values using three variables
temp = num1
num1 = num2
num2 = temp

print("")
print("<------ After swapping ------->")
print(f"first number: {num1}\nSecond number: {num2}")
