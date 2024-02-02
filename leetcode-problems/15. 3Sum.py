class Solution:
    def threeSum(self, nums):
        output = []

        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = n + nums[left] + nums[right]
                if sum == 0:
                    if [n, nums[left], nums[right]] not in output:
                        output.append([n, nums[left], nums[right]])
                    left += 1 
                    right -= 1
                elif sum > 0:
                    right -= 1
                else: left += 1

        return output