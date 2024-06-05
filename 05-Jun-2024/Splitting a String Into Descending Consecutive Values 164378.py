# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        @cache
        def func(idx, prev):
            if idx == n: return True

            for j in range(idx, n):
                val = int(s[idx:j+1])

                if (prev - val) == 1 and func(j+1, val):
                    return True

            return False

        for i in range(n-1):
            val = int(s[:i+1])
            if func(i + 1, val): return True

        return False
