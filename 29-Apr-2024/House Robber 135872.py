# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def func(self,houses, idx, memo):
        if idx >= len(houses):
            return 0
        
        if idx in memo:
            return memo[idx]
        else:
            op_1 = self.func(houses, idx + 1, memo)
            op_2 = houses[idx] + self.func(houses, idx+2, memo)
            memo[idx] = max(op_1, op_2)
            return memo[idx]

    def rob(self, nums: List[int]) -> int:
        return self.func(nums, 0, {})
        