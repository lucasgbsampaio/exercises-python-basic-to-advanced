N, X = map(int, input().split())

marks = []
for i in range(X):
    marks.append(map(float, input().split()))

for j in zip(*marks):
    print(sum(j)/len(j))
