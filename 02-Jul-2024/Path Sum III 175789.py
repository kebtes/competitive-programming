# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1

        def func(root, total=0):
            count = 0

            if root:
                total += root.val
                count = sum_cnt[total - targetSum]
                sum_cnt[total] += 1

                count += func(root.left, total) + func(root.right, total)
                sum_cnt[total] -= 1

            return count

        return func(root)
