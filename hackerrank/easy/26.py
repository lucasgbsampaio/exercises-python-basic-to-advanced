"""
Task
Read four numbers, a, b, c, and d, and print the result of a**b + c**d.
"""

a, b, c, d = (int(input()) for i in range(4))

print(pow(a, b)+pow(c, d))