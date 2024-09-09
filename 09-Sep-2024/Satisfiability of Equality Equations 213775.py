# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = defaultdict(str)
        rank = defaultdict(int)

        def find(node):
            if node not in parent:
                parent[node] = node
                
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node_1, node_2):
            parent_X = find(node_1)
            parent_Y = find(node_2)

            if parent_X != parent_Y:
                if rank[parent_Y] > rank[parent_X]:
                    parent[parent_X] = parent_Y
                elif rank[parent_Y] < rank[parent_X]:
                    parent[parent_Y] = parent_X
                else:
                    parent[parent_X] = parent_Y
                    rank[parent_X] += 1

        for eq in equations:
            if "==" in eq:
                a, b = eq.split("==")
                union(a,b)

        for eq in equations:
            if "!=" in eq:
                a, b = eq.split("!=")
                root_1 = find(a)
                root_2 = find(b)
                
                if root_1 == root_2:
                    return False

        return True
