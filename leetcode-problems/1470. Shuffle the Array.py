class Solution:
    def shuffle(self, nums, n):
        merged = []

        for i in range(n):
            merged.append(nums[i])
            merged.append(nums[i+1])

        return merged