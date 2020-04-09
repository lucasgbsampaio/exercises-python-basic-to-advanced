"""
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type.
The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
"""

student_marks = {}
for i in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

student_name = input()
for key, value in student_marks.items():
    if key == student_name:
        print('{:.2f}'.format((sum(value))/3))
