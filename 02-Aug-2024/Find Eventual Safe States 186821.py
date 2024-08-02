# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        node_saftey = {}
        output = []

        def func(node):
            if node in node_saftey:
                return node_saftey[node]

            node_saftey[node] = False

            for neighbor in graph[node]:
                if not func(neighbor):
                    return False

            node_saftey[node] = True
            return True

        for node in range(n):
            if func(node):
                output.append(node)

        return output
