# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []

        for idx in range(n):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                output[stack_idx] = idx - stack_idx

            stack.append(idx)

        return output    