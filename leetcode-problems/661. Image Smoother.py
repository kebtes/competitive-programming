class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        output = [[None]* cols for _ in range(rows)]

        for row in range(rows):
            for column in range(cols):
                t = 0
                c = 0
                for row_idx in range(max(0, row - 1), min(row + 2, rows)):
                    for col_idx in range(max(0, column - 1), min(column + 2, cols)):
                        t += img[row_idx][col_idx]
                        c += 1

                output[row][column] = t // c

        return output