"""
Read an integer N.
Without using any string methods, try to print the following:
1,2,3...N
Note that "..." represents the values in between.
"""

n = int(input().strip())

for num in range(1, n+1):
    print(num, end='')