class Solution:
    def twoSum(self, nums, target):
        numMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in numMap:
                return [numMap[comp], i]
            
            numMap[nums[i]] = i

        return []