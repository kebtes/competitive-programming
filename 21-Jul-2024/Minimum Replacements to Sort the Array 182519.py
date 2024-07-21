# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0

        for i in range(len(nums) - 2, -1, -1):  
            if nums[i] > nums[i + 1]:
                parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]  
                new_value = nums[i] // parts
                op += parts - 1  
                nums[i] = new_value  
        
        return op