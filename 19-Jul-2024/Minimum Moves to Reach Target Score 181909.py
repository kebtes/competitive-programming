# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num_moves = 0

        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                target = target // 2
                maxDoubles -= 1
            else:
                target -= 1

            num_moves += 1

        num_moves += (target - 1)  

        return num_moves