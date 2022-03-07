"""
You are given three integers x,y and z representing the dimensions of a cuboid along with an integers n.

Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n. 

Here, 0 <= i <= x; 0 <= j <=y; 0 <= k <= z;

Example:
x = 1
y = 1
z = 2
n = 3

Print an array of the elements that do not sum to n = 3

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


# method-1: without using list comprehension
    i, j, k = 0, 0, 0
    coordinate = []

    for i1 in range(0, x + 1):
        for j1 in range(0, y + 1):
            for k1 in range(0, z + 1):
                if(x >= 0 and i <= x):
                    coordinate.append(i1)

                if(y >= 0 and j <= y):
                    coordinate.append(j1)

                if(z >= 0 and k <= z):
                    coordinate.append(k1)

    theList = coordinate
    N = 3

    # creating sublist of list
    coordinate_list = [theList[n:n+N] for n in range(0, len(theList), N)]

    result = []
    for list1 in coordinate_list:
        if sum(list1) != n:
            result.append(list1)

    print(result)


# method-2: by using list comprehension
x, y, z, n = (int(input()) for _ in range(4))
print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1)
      for c in range(0, z + 1) if a + b + c != n])
