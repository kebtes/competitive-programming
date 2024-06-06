# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        n = len(nums)

        def func(current_idx, subsets=[]):
            for idx in range(current_idx, n):
                subsets.append(nums[idx])
                output.append(subsets[:])
                func(idx + 1, subsets)
                subsets.pop()

        func(0, [])

        return output