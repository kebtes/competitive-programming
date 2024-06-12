# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

n = int(input())

edges = []

for _ in range(n):
    edge = list(map(int, input().split()))
    edges.append(edge)

cnt = 0
for i in range(n):
    for j in range(n):
        if edges[i][j] == 1:
            cnt += 1

print(cnt//2)