# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        output = []
        has_incoming_edges = set()

        for _, to in edges:
            has_incoming_edges.add(to)

        for v in range(n):
            if v not in has_incoming_edges:
                output.append(v)

        return output

