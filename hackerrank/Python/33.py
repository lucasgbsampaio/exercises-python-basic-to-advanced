"""
collections.namedtuple()
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple

Task

Dr. John Wesley has a spreadsheet containing a list of student's IDS,marks , class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

average =  sum of all marks / total students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks,IDS ,name  and class, under their respective column names.

Output Format

Print the average marks of the list corrected to 2 decimal places.
"""
from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input())
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))