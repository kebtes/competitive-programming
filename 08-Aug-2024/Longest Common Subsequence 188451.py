# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def func(idx_1, idx_2):
            if idx_1 == len(text1) or idx_2 == len(text2):
                return 0
            
            if text1[idx_1] == text2[idx_2]:
                return 1 + func(idx_1 + 1, idx_2 + 1)

            return max(func(idx_1 + 1, idx_2), func(idx_1, idx_2 + 1))
        
        return func(0,0)
        