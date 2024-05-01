# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def func(self, nums, idx, cum_sum, target, memo):
        if idx == len(nums):
            if cum_sum == target:
                return 1
            else:
                return 0

        if (idx, cum_sum) not in memo:
            op_1 = self.func(nums, idx + 1, cum_sum + nums[idx], target, memo)
            op_2 = self.func(nums, idx + 1, cum_sum - nums[idx], target, memo)

            memo[(idx, cum_sum)] = op_1 + op_2 

        return memo[(idx, cum_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.func(nums, 0, 0, target, {})