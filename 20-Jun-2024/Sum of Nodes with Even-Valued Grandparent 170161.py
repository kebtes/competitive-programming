# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # def func(node, cur_sum=0):
        #     if not node:
        #         return 0

        #     if node.val % 2 == 0:
        #         if node.left:
        #             if node.left.left:
        #                 cur_sum += node.left.left.val
        #             if node.left.right:
        #                 cur_sum += node.left.right.val

        #         if node.right:
        #             if node.right.left:
        #                 cur_sum += node.right.left.val
        #             if node.right.right:
        #                 cur_sum += node.right.right.val

        #     cur_sum += func(node.left)
        #     cur_sum += func(node.right)

        #     return cur_sum
        
        def func(node, parent=None, grand_parent=None):
            if not node:
                return 0

            summ = 0

            if grand_parent and grand_parent.val % 2 == 0:
                summ += node.val

            summ += func(node.left, node, parent)
            summ += func(node.right, node, parent)

            return summ

        return func(root)
