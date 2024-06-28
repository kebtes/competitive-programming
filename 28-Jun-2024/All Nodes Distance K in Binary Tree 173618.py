# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        target_node = None 
        parent = {}

        def dfs(node, prev=None):
            nonlocal target_node
            if not node:
                return

            if prev:
                parent[node] = prev

            if node.val == target.val:
                target_node = node
                return

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)
        # print(target_node)

        def bfs(root):
            queue = deque([(root, 0)])
            output = []
            visited = set()
            visited.add(root)

            while queue:
                node, level = queue.popleft()

                if level == k:
                    output.append(node.val) 

                elif level < k:
                    if node.left and node.left not in visited:
                        visited.add(node)
                        queue.append((node.left, level + 1))
                    
                    if node.right and node.right not in visited:
                        visited.add(node)
                        queue.append((node.right, level + 1))

                    if node in parent and parent[node] not in visited:
                        visited.add(parent[node])
                        queue.append((parent[node], level + 1))

            return output

        if not target_node:
            return []
        return bfs(target_node)


