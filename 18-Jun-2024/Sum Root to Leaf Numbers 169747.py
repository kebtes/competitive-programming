# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = 0

        if not root: return output

        def func(node, path):
            nonlocal output
            if node.left:
                func(node.left, path + str(node.left.val))

            if node.right:
                func(node.right, path + str(node.right.val))
            
            if not node.right and not node.left:
                output += int(path)
                
        func(root, str(root.val))
        return output

        