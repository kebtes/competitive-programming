# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        for i in range(n):
            num = abs(nums[i])

            if nums[num - 1] < 0:
                output.append(num)
            else:
                nums[num - 1] *= -1

        return output