# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def func(current_num, combination=[]):
            if len(combination) == k:
                output.append(combination.copy())
                return

            for num in range(current_num, n+1):
                combination.append(num)
                func(num+1, combination)
                combination.pop()

        func(1)
        return output

