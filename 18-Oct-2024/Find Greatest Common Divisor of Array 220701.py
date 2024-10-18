# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def func(a, b):
            if(b == 0):
                return abs(a)
            else:
                return func(b, a % b)

        nums = sorted(nums)
        a = nums[0]
        b = nums[-1]

        return func(a,b)

        