# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def func(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0

            if k == 0:
                return 1

            p = 0
            p += func(r-2,c+1,k-1)
            p += func(r-2,c-1,k-1)
            p += func(r+1,c-2,k-1)
            p += func(r-1,c-2,k-1)
            p += func(r+2,c+1,k-1)
            p += func(r+2,c-1,k-1)
            p += func(r+1,c+2,k-1)
            p += func(r-1,c+2,k-1)

            return p / 8

        return func(row, column, k)

        
            