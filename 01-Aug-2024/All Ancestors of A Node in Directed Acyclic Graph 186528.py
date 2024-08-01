# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        output = [[] for _ in range(n)]

        for f, t in edges:
            graph[t].append(f)
        
        memo = {}

        def dfs(node, visited):
            if node in memo:
                return memo[node]

            ancestors = set()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ancestors.add(neighbor)
                    ancestors.update(dfs(neighbor, visited))
                    visited.remove(neighbor)
            
            memo[node] = ancestors
            return ancestors

        for node in range(n):
            v = set()
            output[node] = sorted(list(dfs(node, v)))

        return output
