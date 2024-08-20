# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)

        # @cache
        # def func(idx, first_house_taken=False):
        #     if idx >= n:
        #         return 0

        #     if idx == n - 1 and first_house_taken:
        #         return 0

        #     op_1 = nums[idx] + func(idx + 2, first_house_taken or idx == 0)
        #     op_2 = func(idx + 1, first_house_taken)

        #     return max(op_1, op_2)

        # return func(0)

        if len(nums) < 3:
            return max(nums)

        def func(h):
            dp1, dp2 = h[0], max(h[:2])

            for amount in h[2:]:
                temp = max(dp2, dp1 + amount)
                dp1 = dp2
                dp2 = temp

            return dp2

        return max(func(nums[:-1]), func(nums[1:]))
