# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def func(root, max_depth):
            if not root:
                return max_depth 

            max_depth += 1
            return max(func(root.left, max_depth),
                        func(root.right, max_depth))

        return func(root, 0)

            

            
        