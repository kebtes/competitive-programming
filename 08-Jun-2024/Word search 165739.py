# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        seen_paths = set()

        def dfs(row, col, i):
            if i == len(word):
                return True

            if row >= rows or row < 0 or col >= cols or col < 0 or board[row][col] != word[i] or (row, col) in seen_paths:
                return False

            seen_paths.add((row, col))

            result = (dfs(row + 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col - 1, i + 1)) 

            seen_paths.remove((row, col))
            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False