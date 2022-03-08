from operator import itemgetter

'''
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

students = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

'''

# n = int(input())
# students = [[input(), float(input())] for _ in range(n)]


students = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# method-1
seconar_elm = sorted(list(set([marks for name, marks in students])))
student_with_second_list_marks = "\n".join(
    [a for a, b in students if b == seconar_elm[1]])

myList = list(student_with_second_list_marks.split("\n"))
myList.sort()

for name in myList:
    # print(name)
    pass


# method-2
lowest = sorted(set(map(itemgetter(1), students)))[1]
for student in sorted(filter(lambda l: l[1] == lowest, students)):
    print(student[0])
