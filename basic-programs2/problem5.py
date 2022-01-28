# Python Program to Solve Quadratic Equation
''' 
    Quadratic equation
    ax^2  + bx + c = 0

    if b**2 - 4ac = 0: roots are equal i.e -b/2

    if b^2 - 4ac > 0: roots are distinct i.e -b/2 +- sqrt(b^2 - 4ac)/2*a
    else: roots are complex 

'''

# co-efficient of quadratic equation are
from cmath import sqrt

a = 2
b = 2
c = 2

# calculate discriminant
disc = (b**2) - (4*a*c)

print(disc)
if disc == 0:
    print("Roots are equal")
    root = -b/2
    print("Root is: ", root)
elif disc > 0:
    print("Roots are distinct")

    root1 = -b/2 + sqrt(disc) / (2 * a)
    root2 = -b/2 - sqrt(disc) / (2*a)

    print("Root1 = ", root1, "\nRoot2 = ", root2)
else:
    print("Roots are complex")
    root1 = -b/2 + sqrt(disc) / (2 * a)
    root2 = -b/2 - sqrt(disc) / (2*a)

    print("Root1 = ", root1, "\nRoot2 = ", root2)
