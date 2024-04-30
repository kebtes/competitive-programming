# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        else:
            while n > 2:
                n = n/3
            return n == 1