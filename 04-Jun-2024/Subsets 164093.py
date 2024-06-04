# Problem: Subsets - https://leetcode.com/problems/subsets/

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for i in range(1, len(nums)+1):
            sub = list(combinations(nums, i))
            subsets.extend([list(comb) for comb in sub])

        return subsets