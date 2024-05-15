# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traversal(root):
            if not root: 
                return

            traversal(root.left)
            traversal(root.right)
            output.append(root.val)

        traversal(root)
        return output