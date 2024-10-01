# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_length = 0

        @cache
        def dfs(r, c):
            max_path = 1
            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if 0 <= nx < ROW and 0 <= ny < COL and matrix[nx][ny] > matrix[r][c]:
                    max_path = max(
                        1 + dfs(nx, ny),
                        max_path
                        )
    
            return max_path
            
        for r in range(ROW):
            for c in range(COL):
                max_length = max(
                    dfs(r, c),
                    max_length
                )

        return max_length

        