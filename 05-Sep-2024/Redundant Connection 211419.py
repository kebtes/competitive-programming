# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node != root[node]:
                node = root[node]

            return node

        def union(n_1, n_2):
            p_1, p_2 = find(n_1 - 1), find(n_2 - 1)

            if p_1 == p_2:
                return False

            if rank[p_1] > rank[p_2]:
                root[p_2] = p_1
                rank[p_1] += rank[p_2]

            else:
                root[p_1] = p_2
                rank[p_2] += rank[p_2]

            return True

        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return [node_1, node_2] 
        