class Solution:
    def threeSumClosest(self, nums, target):
        closest = float('inf')  

        nums = sorted(nums)

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s  
                elif abs(s - target) < abs(closest - target):
                    closest = s
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return closest  
    