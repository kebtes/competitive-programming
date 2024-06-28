# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW = len(mat)
        COL = len(mat[0])

        queue = deque()

        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float('inf')

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r, c = queue.popleft()

            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if 0 <= nx < ROW and 0 <= ny < COL and mat[nx][ny] > mat[r][c] + 1:
                    queue.append((nx, ny))
                    mat[nx][ny] = mat[r][c] + 1

        return mat 


