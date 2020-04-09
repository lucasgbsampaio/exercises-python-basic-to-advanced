from collections import deque

d = deque()
for _ in range(int(input())):
    eval("d.{}({})".format(*input().split()+['']))

print(*[i for i in d])