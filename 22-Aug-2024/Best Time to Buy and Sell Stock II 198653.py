# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        prev = prices[0]

        for i in range(len(prices)):
            if prev < prices[i]:
                output += prices[i] - prev

            prev = prices[i]

        return output