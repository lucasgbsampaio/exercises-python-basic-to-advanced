"""
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.
"""

N, n = int(input()), input().split()

print(all([int(i) > 0 for i in n])) and any([j == j[::-1] for j in n])

