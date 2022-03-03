"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

Sample value of n is 5
Expected Result : 615
"""

# solution
num = input("Enter a number: ")

num1 = int("%s" % num)
num2 = int("%s%s" % (num, num))
num3 = int("%s%s%s" % (num, num, num))

print(num1 + num2 + num3)
