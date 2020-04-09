"""
Given an integer,n , print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

Input Format

A single integer denoting n.
"""
n = int(input())

width = len(bin(n)[2:])

for i in range(1, n+1):
    print(str(i).rjust(width, ' '), str(oct(i)[2:]).rjust(width, ' '), str(hex(i)[2:].upper()).rjust(width, ' '), str(bin(i)[2:]).rjust(width, ' '), sep=' ')


"""
def print_formatted(number):
    space = len(f"{number+0:b}")
    for i in range(1,number+1):
        print(f"{i+0:{space}d} {i+0:{space}o} {i+0:{space}X} {i+0:{space}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
"""