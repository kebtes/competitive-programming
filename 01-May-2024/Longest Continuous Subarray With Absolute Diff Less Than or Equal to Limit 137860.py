# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing_queue = deque()
        decreasing_queue = deque()
        
        l = 0
        longest_length = 0

        for r in range(len(nums)):
            while increasing_queue and nums[r] < increasing_queue[-1]:
                increasing_queue.pop()
            increasing_queue.append(nums[r])

            while decreasing_queue and nums[r] > decreasing_queue[-1]:
                decreasing_queue.pop()
            decreasing_queue.append(nums[r])

            if increasing_queue[0] - decreasing_queue[0] > limit:
                if increasing_queue[0] == nums[l]:
                    increasing_queue.popleft()
                if decreasing_queue[0] == nums[l]:
                    decreasing_queue.popleft()
                
                l += 1
            
            longest_length = max(longest_length, r - l + 1)
            
        return longest_length