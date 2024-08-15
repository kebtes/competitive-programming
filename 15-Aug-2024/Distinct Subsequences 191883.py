# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def func(pt_1, pt_2):
            if pt_2 == len(t):
                return 1
            
            if pt_1 == len(s):
                return 0

            op_1 = 0
            if s[pt_1] == t[pt_2]:
                op_1 = func(pt_1 + 1, pt_2 + 1)

            op_2 = func(pt_1 + 1, pt_2)

            return op_1 + op_2

        return func(0, 0)

