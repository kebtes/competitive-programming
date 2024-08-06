# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def func(self, n, memo):
        if n <= 1:
            return 1

        if n not in memo:
            memo[n] = self.func(n-1, memo) + self.func(n-2, memo)
        
        return memo[n]

    def climbStairs(self, n: int) -> int:
        return self.func(n, {})