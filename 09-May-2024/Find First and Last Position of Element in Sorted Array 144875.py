# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1,-1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            pivot = (l + r) // 2

            if nums[pivot] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        if 0 <= l < len(nums) and nums[l] == target:
            output[0] = l

        l = 0
        r = len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2

            if nums[pivot] <= target:
                l = pivot + 1
            else:
                r = pivot - 1

        if 0 <= r < len(nums) and nums[r] == target:
            output[1] = r

        return output


