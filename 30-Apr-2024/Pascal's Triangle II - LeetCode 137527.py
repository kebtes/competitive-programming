# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1], [1,1]]

        for i in range(2, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, len(row) - 1):
                row[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(row)

        return dp[rowIndex]
        