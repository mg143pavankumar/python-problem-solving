"""
Example:
    2 
    har 25 26.5 28
    kam 24 26 28
    har

    average of marks for particular student

"""


n = int(input())
student_marks = {}

for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()

a, b, c = student_marks[query_name]
print("%.2f" % ((a + b + c) / 3))
