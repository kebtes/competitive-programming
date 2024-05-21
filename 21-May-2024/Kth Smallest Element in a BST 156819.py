# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def func(root):
            if not root:
                return []
            
            return func(root.left) + [root.val] + func(root.right)
        
        sorted_elements = func(root)
        return sorted_elements[k-1]
        