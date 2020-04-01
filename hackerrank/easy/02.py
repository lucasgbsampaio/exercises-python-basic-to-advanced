"""
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""

a = int(input().strip())
b = int(input().strip())

print(a+b)
print(a-b)
print(a*b)