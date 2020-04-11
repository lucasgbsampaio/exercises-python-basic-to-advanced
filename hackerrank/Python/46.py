N, M = input().split()

elements_array = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in elements_array]))