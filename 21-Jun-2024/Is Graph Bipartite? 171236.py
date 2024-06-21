# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = defaultdict(int)
        # visited = {}

        def func(node, expected_value = 1):
            if node in visited:
                return visited[node] == expected_value

            visited[node] = expected_value

            for edge in graph[node]:
                if not func(edge, expected_value * -1):
                    return False
            
            return True

        for node in range(len(graph)):
            if node not in visited and not func(node):    
                return False

        return True     