"""
Write a Python program which accepts the radius of a circle from the user and compute the area.

Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

# solution
import math

radius = float(input("Enter the radius of the circle: "))


def area_of_circle(radius):
    return math.pi * radius * radius


print(area_of_circle(radius))
