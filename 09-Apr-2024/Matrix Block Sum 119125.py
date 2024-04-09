# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])

        output = [[0] * COL for _ in range(ROW)]
        prefix = [[0] * (COL + 1) for _ in range(ROW + 1)]
        
        for i in range(1, ROW + 1):
            for j in range(1, COL + 1):

                prefix[i][j] = (
                    prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )
        for i in range(ROW):
            for j in range(COL):

                row_1 = max(0, i - k)
                row_2 = min(ROW, i + k + 1)
                col_1 = max(0, j - k)
                col_2 = min(COL, j + k + 1)
                output[i][j] = (
                    prefix[row_2][col_2]

                    - prefix[row_2][col_1]
                    - prefix[row_1][col_2]
                    + prefix[row_1][col_1]
                )

        return output
