class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def hcfnaive(a, b):
            if(b == 0):
                return abs(a)
            else:
                return hcfnaive(b, a % b)

        nums = sorted(nums)
        a = nums[0]
        b = nums[-1]

        return hcfnaive(a,b)

        