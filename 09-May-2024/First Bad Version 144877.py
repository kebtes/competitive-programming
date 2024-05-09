# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l < r:
            pivot = (l + r ) // 2

            if isBadVersion(pivot):
                r = pivot
            else:
                l = pivot + 1

        return r