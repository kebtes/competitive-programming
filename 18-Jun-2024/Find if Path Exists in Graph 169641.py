# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = [False] * n

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        def func(node, destination, graph, visited):
            if node == destination:
                return True

            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if func(neighbor, destination, graph, visited):
                        return True

            return False

        return func(source, destination, graph, visited)
