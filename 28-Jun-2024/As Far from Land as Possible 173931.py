# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        output = -1
        visited = set()

        N = len(grid)
        queue = deque((i, j, 0) for i in range(N) for j in range(N) if grid[i][j])

        # for r in range(N):
        #     for c in range(N):
        #         if grid[r][c] == 1:
        #             queue.append((r, c, 0))

        if len(queue) in (0, N*N):
            return -1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
        while queue:
            r, c, l = queue.popleft()
            output = max(output, l)

            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    visited.add((nx, ny)) 
                    queue.append((nx, ny, l + 1))

        return output


        