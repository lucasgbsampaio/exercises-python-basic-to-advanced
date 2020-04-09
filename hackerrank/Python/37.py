"""
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
"""

from calendar import weekday, day_name

date = input().split()
week_day = weekday(int(date[2]), int(date[0]), int(date[1]))

print(day_name[week_day].upper())