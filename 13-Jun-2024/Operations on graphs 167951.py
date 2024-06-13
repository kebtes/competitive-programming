# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict

vertices = int(input())
operations = int(input())

graph = defaultdict(list)

for _ in range(operations):
    op, *nums = list(map(int, input().split()))
    
    if op == 1:
        n1, n2 = nums
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    else:
        print(*graph[nums[0]])