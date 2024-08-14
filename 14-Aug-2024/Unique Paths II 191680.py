# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])

        dp = [[0] * COL for _ in range(ROW)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for r in range(1, ROW):
            dp[r][0] = dp[r-1][0] if obstacleGrid[r][0] == 0 else 0

        for c in range(1, COL):
            dp[0][c] = dp[0][c-1] if obstacleGrid[0][c] == 0 else 0
        
        for r in range(1, ROW):
            for c in range(1, COL):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]



                
        