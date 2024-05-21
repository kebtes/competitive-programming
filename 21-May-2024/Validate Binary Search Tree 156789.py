# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def func(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True

            if root.val <= lower or root.val >= upper:
                return False
            
            if not func(root.right, root.val, upper):
                return False
            
            if not func(root.left, lower, root.val):
                return False
            
            return True

        return func(root)