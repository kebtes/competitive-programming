# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        memo = {}
        
        def func(i, W):
            if i >= len(wt) or W == 0:
                return 0
                
            if (i, W) not in memo:
                op_1 = 0
                if wt[i] <= W:
                    op_1 = val[i] + func(i + 1, W - wt[i])
                    
                op_2 = func(i + 1, W)
                
                memo[(i, W)] = max(op_1, op_2)
                
            return memo[(i, W)]
            
        return func(0, W)