# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROW = len(grid)
        COL = len(grid[0])

        figure_direction = {
            1: [[0, -1], [0, 1]],      
            2: [[-1, 0], [1, 0]],      
            3: [[0, -1], [1, 0]],      
            4: [[0, 1], [1, 0]],       
            5: [[0, -1], [-1, 0]],     
            6: [[0, 1], [-1, 0]],      
        }

        def func(r, c, nr, nc):
            if 0 <= nr < ROW and 0 <= nc < COL:
                for d in figure_direction[grid[nr][nc]]:
                    if [r - nr, c - nc] == d:
                        return True
            return False

        def dfs(r, c):
            if r == ROW - 1 and c == COL - 1:
                return True

            visited.add((r, c))
            for dr, dc in figure_direction[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and func(r, c, nr, nc):
                    if dfs(nr, nc):
                        return True
            return False

        visited = set()
        return dfs(0, 0)
