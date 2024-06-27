# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
s, e = map(int, input().split())

if s == e:
    print(0)
    exit()

graph = defaultdict(list)

for _ in range(m):
    from_, to_ = map(int, input().strip().split())
    graph[from_].append(to_)
    graph[to_].append(from_)

queue = deque([s])  
visited = set()
visited.add(s)
parent = {s: None}

is_found = False
while queue and not is_found:
    node = queue.popleft()

    for edge in graph[node]:
        if edge == e:
            parent[edge] = node
            is_found = True
            break

        if edge not in visited:
            queue.append(edge)
            visited.add(edge)
            parent[edge] = node

if not is_found:
    print(-1)
else:
    path = []
    current = e
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path.reverse()  
    print(len(path) - 1)  
    print(*path)