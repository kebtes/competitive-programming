# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        
        def func(start, current_sum, combination=[]):
            if current_sum == target: 
                output.append(combination[:])

            if current_sum > target:
                return 

            for i in range(start, len(candidates)):
                current_num = candidates[i]
                combination.append(current_num)
                func(i, current_sum + current_num, combination)
                combination.pop()
            
        func(0,0,[])
        return output
        