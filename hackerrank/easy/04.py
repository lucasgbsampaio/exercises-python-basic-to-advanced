"""
Read an integer n. For all non-negative integers i<n, print i². See the sample for details.
"""

n = int(input().strip())

for num in range(n):
    print(num*num)