# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left

            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            
            root.val = tmp.val
            root.right = self.deleteNode(root.right, root.val)

        return root

        
            

        