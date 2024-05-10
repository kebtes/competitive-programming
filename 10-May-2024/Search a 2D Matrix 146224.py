# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        def func(row_level):
            l = 0
            r = len(row_level) - 1

            while l <= r:
                mid = (l + r) // 2

                if row_level[mid] == target:
                    return True 
                elif row_level[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        for i in range(row):
            if target >= matrix[i][0] and target <= matrix[i][col - 1]:
                return func(matrix[i])

        return False
