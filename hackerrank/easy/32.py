"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.
"""
from collections import defaultdict

n, m = map(int, input().split())
default = defaultdict(list)
list1 = []

for i in range(1, n+1):
    default[input()].append(str(i))

for j in range(m):
    B = input()
    if B in default:
        print(' '.join(map(str, default[B])))
    else:
        print(-1)