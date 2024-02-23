class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid) 
        col = len(grid[0]) 

        max_sum = 0

        for i in range(row-2):
            for j in range(col-2):
                sum_ = 0

                sum_ += grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                max_sum = max(sum_, max_sum)

        return max_sum

