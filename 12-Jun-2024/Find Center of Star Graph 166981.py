# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = set()

        for edge in edges:
            if edge[0] in connections:
                return edge[0]
            if edge[1] in connections:
                return edge[1]

            connections.add(edge[0])
            connections.add(edge[1])

        
        
        
        