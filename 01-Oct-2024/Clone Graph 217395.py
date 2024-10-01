# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        map = {}
        queue = deque([node])
        map[node] = Node(node.val)
        while queue:
            n = queue.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                map[n].neighbors.append(map[neighbor])

        return map[node]