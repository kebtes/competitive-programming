# Problem: Same Tree - https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def func(t_1, t_2):
            if not t_1 and not t_2:
                return True

            if not t_1 or not t_2:
                return False
            
            return t_1.val == t_2.val and func(t_1.left, t_2.left) and func(t_1.right, t_2.right)

        return func(p, q)

        
        