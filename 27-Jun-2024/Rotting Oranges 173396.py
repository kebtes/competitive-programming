# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        if ROW == 0:
            return -1

        fresh = 0
        rotten = deque()
        output = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while rotten and fresh > 0:
            output += 1
            size = len(rotten)

            for _ in range(size):
                r, c = rotten.popleft()

                for dx, dy in directions:
                    nx, ny = r + dx, c + dy

                    if 0 <= nx < ROW and 0 <= ny < COL and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2
                        rotten.append((nx, ny))

        return output if fresh == 0 else -1
