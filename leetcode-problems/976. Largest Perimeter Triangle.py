class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        length = len(nums)

        for i in range(length - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0