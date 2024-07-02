# Problem: Convert Sorted Array to Binary Search Tree  - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(s, e):
            if s > e: return None

            mid = (s + e) // 2
            root = TreeNode(nums[mid])
            root.left = func(s, mid - 1)
            root.right = func(mid + 1, e)

            return root

        return func(0, len(nums) - 1)