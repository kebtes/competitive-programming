# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        output = 0

        ROW = len(grid)
        COL = len(grid[0])

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    output += 4
                    
                    if row > 0 and grid[row - 1][col] == 1:  
                        output -= 2
                    if col > 0 and grid[row][col - 1] == 1:  
                        output -= 2

        return output
