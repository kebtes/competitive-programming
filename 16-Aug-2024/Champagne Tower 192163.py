# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for _ in range(101)]
        dp[0][0] = poured

        for i in range(100):
            for j in range(i+1):
                if dp[i][j] > 1:
                    overflow = dp[i][j] - 1

                    dp[i+1][j] += overflow / 2
                    dp[i+1][j+1] += overflow / 2

                    dp[i][j] = 1
                
                if j >= query_glass: break

            if i >= query_row: break

        return dp[query_row][query_glass]
                
            


