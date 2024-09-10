# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        i, j = 0, 0

        r = len(matrix)
        c = len(matrix[0])

        visited = set()

        for _ in range(r * c):
            output.append(matrix[i][j])
            visited.add((i, j))

            ni, nj = i + direction[direction_idx][0], j + direction[direction_idx][1]

            if ni < 0 or ni >= r or nj < 0 or nj >= c or (ni, nj) in visited:
                direction_idx = (direction_idx + 1) % 4
                ni, nj = i + direction[direction_idx][0], j + direction[direction_idx][1]

            i, j = ni, nj

        return output
                


        