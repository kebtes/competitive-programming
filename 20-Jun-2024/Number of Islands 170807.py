# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        output = 0

        def func(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] == "0":
                return 

            grid[row][col] = "0"
            
            func(row + 1, col)
            func(row - 1, col)
            func(row, col - 1)
            func(row, col + 1)

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    func(row, col)
                    output += 1

        return output
