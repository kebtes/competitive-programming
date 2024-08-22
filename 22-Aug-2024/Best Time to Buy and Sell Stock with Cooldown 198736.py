# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def func(idx, prev=None):
            if idx >= len(prices):
                return 0

            if prev != None:
                hold = func(idx + 1, prev)
                sell = (prices[idx] - prev) + func(idx + 2, None)
                
                return max(hold, sell)

            else:
                skip = func(idx + 1, None)
                buy = func(idx + 1, prices[idx])
                
                return max(skip, buy)

        return func(0)
