# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        freq_dict = Counter(s)
        odd_taken = False
        max_length = 0

        
        for cnt in freq_dict.values():
            if cnt % 2 == 0:
                max_length += cnt
            else:
                max_length += (cnt - 1)
                odd_taken = True
        
        if odd_taken:
            max_length += 1
            
        return max_length

            





        
        