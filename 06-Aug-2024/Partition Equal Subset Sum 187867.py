# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:    
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def func(idx, target): 
            if target == 0:
                return 1
            if idx == len(nums):
                return 0

            op_1 = 0
            
            if target - nums[idx] >= 0:
                op_1 = func(idx + 1, target - nums[idx])

            return op_1 or func(idx + 1, target)
        
        total = sum(nums)
        nums.sort()

        if total % 2: return False

        return func(0, total//2)