# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        0 1 4 4 5 7

        """
        
        res = 0
        nums.sort()

        for idx, num in enumerate(nums):
            left_idx = bisect.bisect_left(nums, lower - num, lo = idx + 1)
            right_idx = bisect.bisect_right(nums, upper - num, lo = idx + 1)

            res += (right_idx - left_idx)

        return res


            