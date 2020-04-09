"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""

students = []
for n in range(int(input())):
    name = input()
    grade = float(input())
    students.append([name, grade])
print(students)
second_lowest = sorted(set([g for n, g in students]))[1]
print(second_lowest)