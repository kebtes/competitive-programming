# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = {}

        # def dp(index, prev_index):
        #     if index == n:
        #         return 0
            
        #     if (index, prev_index) in memo:
        #         return memo[(index, prev_index)]
            
        #     op_1 = 0
        #     if prev_index == -1 or nums[index] > nums[prev_index]:
        #         op_1 = 1 + dp(index + 1, index)
            
        #     op_2 = dp(index + 1, prev_index)
            
        #     memo[(index, prev_index)] = max(op_1, op_2)
        #     return memo[(index, prev_index)]

        # return dp(0, -1)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        
