class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r_len, c_len = len(matrix), len(matrix[0])

        rows = []
        columns = []

        for r in range(r_len):
            for c in range(c_len):
                if matrix[r][c] == 0:
                    if r not in rows:
                        rows.append(r)
                    if c not in columns:
                        columns.append(c)

        for r in range(r_len):
            for c in range(c_len):
                if r in rows or c in columns:
                    matrix[r][c] = 0