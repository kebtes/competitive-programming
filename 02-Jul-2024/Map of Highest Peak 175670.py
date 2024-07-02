# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW = len(isWater)
        COL = len(isWater[0])

        queue = deque()
        for row in range(ROW):
            for col in range(COL):
                if isWater[row][col] == 1:
                    isWater[row][col] = 0
                    queue.append((row, col))
                else:
                    isWater[row][col] = -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                nx, ny = row + dx, col + dy

                if 0 <= nx < ROW and 0 <= ny < COL and isWater[nx][ny] == -1:
                    isWater[nx][ny] = isWater[row][col] + 1
                    queue.append((nx, ny))

        return isWater
