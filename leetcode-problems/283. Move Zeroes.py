class Solution:
    def moveZeroes(self, nums):
        h = 0
        
        for i in range(len(nums) - 1):
            if nums[i] != 0:
                nums[i], nums[h] = nums[h], nums[i]
                h += 1
        
