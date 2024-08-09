# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def func(amnt, memo={}):
            if amnt == 0: return 0
            if amnt < 0: return float('inf')

            op = float('inf')

            if amnt not in memo:
                for coin in coins:
                    op = min(op, func(amnt - coin, memo) + 1)

                memo[amnt] = op

            return memo[amnt]
    
        res = func(amount)
        return -1 if res == float('inf') else res
            