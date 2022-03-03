"""
Write a Python program to accept a filename from the user and print the extension of that.

Sample filename : abc.java
Output : java
"""


# solution

file_name = input("Enter the filename: ")

file_extension = file_name.split(".")
print(file_extension[-1])
