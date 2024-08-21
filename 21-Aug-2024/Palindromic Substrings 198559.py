# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        output = 0

        def func(l, r):
            cnt = 0

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

                cnt += 1

            return cnt

        for i in range(n):
            e = func(i, i + 1)
            o = func(i, i)

            output += (e + o)

        return output