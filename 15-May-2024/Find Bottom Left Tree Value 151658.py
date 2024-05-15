# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        last_left_val = 0

        def func(root, depth):
            nonlocal max_depth, last_left_val

            if not root:
                return

            if depth > max_depth:
                max_depth = depth
                last_left_val = root.val

            func(root.left, depth + 1)
            func(root.right, depth + 1)
        
        func(root, 0)
        return last_left_val

            

            
            
        