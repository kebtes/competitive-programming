# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        tb = [0] * (n + 2)

        for i in range(n-1, -1, -1):
            tb[i] = max(nums[i] + tb[i+2], tb[i+1])

        return tb[0]
        