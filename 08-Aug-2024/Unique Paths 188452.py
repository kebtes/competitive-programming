# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def func(m,n):
            if m == 0 or n == 0: return 0
            if m == 1 or m == 1: return 1

            return func(m-1, n) + func(m, n-1)

        return func(m,n)

        