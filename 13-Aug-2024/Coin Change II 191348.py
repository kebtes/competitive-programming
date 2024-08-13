# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def func(idx, remaining):
            if remaining == 0: return 1
    
            if remaining < 0 or idx == len(coins): 
                return 0
            
            if (idx, remaining) in memo:
                return memo[(idx, remaining)]
            
            op_1 = func(idx, remaining - coins[idx])
            op_2 = func(idx + 1, remaining)
    
            memo[(idx, remaining)] = op_1 + op_2
            return memo[(idx, remaining)]
        
    
        return func(0, amount)