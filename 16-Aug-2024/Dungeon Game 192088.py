# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        ROW = len(dungeon)
        COL = len(dungeon[0])

        @cache
        def func(r, c):
            if r == ROW or c == COL:
                return float('inf')

            if r == ROW - 1 and c == COL - 1:
                return max(1, 1 - dungeon[r][c])

            op_1 = func(r + 1, c)
            op_2 = func(r, c + 1)

            return max(1, min(op_1, op_2) - dungeon[r][c])

        return func(0, 0)
