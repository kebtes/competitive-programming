# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        m_length = 0
        
        @cache
        def func(idx: int) -> int:
            nonlocal m_length
            
            l = 1  
            
            for prev in range(idx):
                if nums[idx] > nums[prev]:
                    l = max(l, func(prev) + 1)
            
            m_length = max(m_length, l)
            return l
        
        for i in range(n):
            func(i)
        
        @cache
        def counter(idx: int) -> int:
            if func(idx) == 1:
                return 1  
            
            total_count = 0
            for prev in range(idx):
                if nums[idx] > nums[prev] and func(prev) == func(idx) - 1:
                    total_count += counter(prev)
            
            return total_count
        
        output = 0
        for i in range(n):
            if func(i) == m_length:
                output += counter(i)
        
        return output
