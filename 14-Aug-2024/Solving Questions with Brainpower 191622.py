# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # @cache
        # def func(idx):
        #     if idx >= len(questions):
        #         return 0

        #     op_1 = questions[idx][0] + func(idx + questions[idx][1] + 1)
        #     op_2 = func(idx + 1)

        #     return max(op_1, op_2)

        # return func(0)

        N = len(questions)
        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            p, j = questions[i][0], questions[i][1]
            
            nxt_idx = min(N, i + j + 1)
            dp[i] = max(dp[i+1], p + dp[nxt_idx])

        return dp[0]

            

            



        