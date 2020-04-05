"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""

string = input().strip()
sub_string = input().strip()

count = 0
for i in range(len(string)-len(sub_string)+1):
    if string[i] == sub_string[0]:
        flag = 1
        for j in range(len(sub_string)):
            if string[i + j] != sub_string[j]:
                flag = 0
                print(f'valor: {sub_string[j]}')
                break
        if flag == 1:
            count = count + 1
print(count)