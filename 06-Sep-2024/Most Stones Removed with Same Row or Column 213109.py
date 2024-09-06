# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])  
                
            return parents[node]

        def union(node_1, node_2):
            parent_1 = find(node_1)
            parent_2 = find(node_2)

            if parent_1 != parent_2:
                if rank[parent_1] == rank[parent_2]:
                    parents[parent_1] = parent_2
                    rank[parent_1] += rank[parent_2]
                
                elif rank[parent_1] > rank[parent_2]:
                    parents[parent_2] = parent_1
                
                else:
                    parents[parent_1] = parent_2

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[j][1] == stones[i][1]:
                    union(i,j)

        unique_parent = set(find(i) for i in range(n))
        return n - len(unique_parent)

                