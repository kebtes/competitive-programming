# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])    

        dp = [[0] * ROW for _ in range(COL)]
        dp[0] = matrix[0]

        for r in range(1, ROW):
            for c in range(COL):
                local_min = float('inf')

                if c - 1 >= 0:
                    local_min = min(local_min, dp[r-1][c-1] + matrix[r][c])

                if c + 1 < COL:
                    local_min = min(local_min, dp[r-1][c+1] + matrix[r][c])

                local_min = min(local_min, dp[r-1][c] + matrix[r][c])
                dp[r][c] = local_min

        return min(dp[-1])

