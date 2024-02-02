class Solution:
    def isMonotonic(self, nums) -> bool:
        is_increasing = None
        is_decreasing = None

        for i in range(len(nums) -1):
            if nums[i] < nums[i+1]:
                is_increasing = True
            if nums[i] > nums[i+1]:
                is_decreasing = True

        if is_increasing and is_decreasing:
            return False
        
        return True