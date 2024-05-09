# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from itertools import accumulate
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = n+1
        prefix_sum = [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        queue = deque()

        for idx, val in enumerate(prefix_sum):
            while queue and val <= prefix_sum[queue[-1]]:
                queue.pop()

            while queue and val - prefix_sum[queue[0]] >= k:
               output = min(output, idx - queue.popleft())
            
            queue.append(idx)

        if output < n+1:
            return output
        return -1