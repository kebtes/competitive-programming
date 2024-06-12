# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder_traversal(root):
            r = []

            if root:
                r = inorder_traversal(root.left)
                r.append(root.val)
                r += inorder_traversal(root.right)
            
            return r

        def build_tree(sorted_list):
            if not sorted_list:
                return None

            mid = len(sorted_list) // 2
            root = TreeNode(sorted_list[mid])
            root.left = build_tree(sorted_list[:mid])
            root.right = build_tree(sorted_list[mid + 1: ])

            return root

        return build_tree(inorder_traversal(root))