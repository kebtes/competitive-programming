# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        l = 0

        for num in nums:
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            max_queue.append(num)

            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            min_queue.append(num)

            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                
                l += 1
            
        return len(nums) - l