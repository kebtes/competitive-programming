# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1

        n1, n2, n3 = 0, 1, 1

        for i in range(2, n):
            n1, n2, n3 = n2, n3, n1 + n2 + n3

        return n3
        