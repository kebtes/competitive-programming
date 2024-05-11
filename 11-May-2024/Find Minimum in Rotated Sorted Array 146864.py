# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while l+1 < r:
            mid = (l + r) // 2

            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid

        return nums[r]
