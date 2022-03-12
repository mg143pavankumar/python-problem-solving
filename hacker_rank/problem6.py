'''
Given an integer, n, and n space-separated integers as input, 
create a tuple, t of those n integers. Then computer and print
the result of hash(i)

'''

print(input() == 0 or hash(tuple(map(int, input().split(" ")))))
