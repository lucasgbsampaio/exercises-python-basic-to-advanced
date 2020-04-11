import re

lst = list()
for i in range(int(input())):
    lst.append(input())

print(sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$', x), lst))))