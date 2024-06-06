# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        best = ""

        @cache
        def good(start, end):
            t = set(s[start:end])

            for x in t:
                if (x.lower() in t) != (x.upper() in t):
                    return False

            return True
   
        for start in range(n+1):
            for end in range(start+1, n+1):
                if good(start, end) and end-start > len(best):
                    best = s[start:end]

        return best