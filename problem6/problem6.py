"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

# solution
data = input("Enter a sequence of comma-separated numbers: ")

new_data = data.split(",")
list_data = list(new_data)
tuple_data = tuple(new_data)

print("List: ", list_data)
print("Tuple: ", tuple_data)
