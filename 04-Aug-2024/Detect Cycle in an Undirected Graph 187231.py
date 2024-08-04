# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited_ = [False] * V  

        def dfs(node, parent):
            visited_[node] = True
            
            for neighbor in adj[node]:
                if not visited_[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
        for i in range(V):
            if not visited_[i]:
                if dfs(i, -1):
                    return True
                    
        return False