class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def minimum_moves(target_1, target_2 = target):
            return abs(target_1[0] - target_2[0]) + abs(target_1[1] - target_2[1])
            
        # mini = minimum_moves([0,0])

        for ghost in ghosts:
            if minimum_moves(ghost) <= minimum_moves([0,0]):
                return False

        return True