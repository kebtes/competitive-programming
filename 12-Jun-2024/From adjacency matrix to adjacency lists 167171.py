# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

from collections import defaultdict

n = int(input())

matrix = []

for _ in range(n):
    c = list(map(int, input().split()))
    matrix.append(c)

edges = defaultdict(list)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            edges[i+1].append(j+1)

for edge in edges:
    print(len(edges[edge]), *edges[edge])