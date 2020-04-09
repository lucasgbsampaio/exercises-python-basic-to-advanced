"""
The first line contains a string, S.
The second line contains the width, W .
"""

string = input()
width = int(input())

for i in range(0, len(string), width):
    print(string[i:i+width])
