class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid) 
        col = len(grid[0]) 

        max_sum = 0

        for i in range(row):
            for j in range(col):
                sum_ = 0

                if i + 2 > row - 1 or j + 2 > col - 1:
                    continue

                sum_ += sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1]
                max_sum = max(sum_, max_sum)

        return max_sum

