# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        def func(row, cols, diag_1, diag_2, combination):
            if row == n:
                result = []
                for row in combination:
                    result.append("".join(row))
                
                output.append(result)
                return

            for col in range(n):
                d1 = col - row
                d2 = row + col

                if col not in cols and d1 not in diag_1 and d2 not in diag_2:
                    diag_1.add(d1)
                    diag_2.add(d2)
                    cols.add(col)
                    combination[row][col] = "Q"

                    func(row + 1, cols, diag_1, diag_2, combination)

                    diag_1.remove(d1)
                    diag_2.remove(d2)
                    cols.remove(col)
                    combination[row][col] = "."
        
        empty_board = [['.'] * n for _ in range(n)]
        func(0, set(), set(), set(), empty_board)
        return output