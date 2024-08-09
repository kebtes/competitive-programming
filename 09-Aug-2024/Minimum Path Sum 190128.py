# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        @cache
        def func(r, c):
            if r >= ROW or c >= COL:
                return float('inf')
            
            if r == ROW - 1 and c == COL - 1:
                return grid[r][c]

            op_1 = func(r + 1, c)
            op_2 = func(r, c + 1)

            return grid[r][c] + min(op_1, op_2)
    
        return func(0,0)