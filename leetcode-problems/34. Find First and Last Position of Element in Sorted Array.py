class Solution:
    def searchRange(self, nums, target):
        output = [0,0]

        if target not in nums:
            return [-1,-1]
        
        for i, n in enumerate(nums):
            if n == target: 
                output[0] = i
                break
    
        for i in range(output[0], len(nums)):
            if nums[i] == target:
                output[1] = i
    
        return output
    