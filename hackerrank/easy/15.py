"""
Read a given string, change the character at a given index and then print the modified string.
"""

string = list(input())
index, character = input().split()

string[int(index)] = character
print(''.join(string))
