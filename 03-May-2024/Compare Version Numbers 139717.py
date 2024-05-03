# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        for v1, v2 in zip_longest(version1, version2, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0