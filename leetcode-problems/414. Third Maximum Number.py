class Solution:
    def thirdMax(self, nums):
        third_max = 0
        maximum = None 

        if len(nums) < 3:
            nums = sorted(nums, reverse=True)
            return nums[0]

        for _ in range(3):
            if len(nums) < 1:
                return maximum
            
            nums = sorted(nums, reverse=True)
            third_max = nums[0]

            if not maximum: maximum = third_max

            nums = [x for x in nums if x!= third_max]

        return third_max
