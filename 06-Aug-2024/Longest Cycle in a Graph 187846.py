# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        
        visited = [False] * n
        on_stack = [False] * n
        
        stack = []
        output = -1

        def dfs(node):
            nonlocal output
            
            visited[node] = True
            on_stack[node] = True
            stack.append(node)

            next_node = edges[node]
            if next_node != -1:
                if not visited[next_node]:
                    dfs(next_node)
                elif on_stack[next_node]:
                    cycle_start = stack.index(next_node)
                    output = max(output, len(stack) - cycle_start)

            stack.pop()
            on_stack[node] = False

        for node in range(n):
            if not visited[node]:
                dfs(node)

        return output