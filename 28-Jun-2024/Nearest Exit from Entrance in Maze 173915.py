# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        output = 0
        queue = deque([(entrance[0], entrance[1], 0)])

        ROW = len(maze)
        COL = len(maze[0])
        
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, l = queue.popleft()

            if [r,c] != entrance and (r == 0 or r == (ROW - 1) or c == 0 or c == (COL - 1)) and maze[r][c] == '.':
                return l

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if (0 <= nx < ROW and 0 <= ny < COL) and (nx, ny) not in visited and maze[nx][ny] != "+":
                    queue.append((nx, ny, l + 1))
                    visited.add((nx, ny))

        return -1



        