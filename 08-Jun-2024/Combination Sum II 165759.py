# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        def func(i, current_sum, combination = []):
            if current_sum > target:
                return

            if current_sum == target:
                output.append(combination[:])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                    
                combination.append(candidates[j])
                func(j + 1, current_sum + candidates[j], combination)
                combination.pop()

        func(0,0)
        return output