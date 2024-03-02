class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        output = 0
        idx = 1

        for _ in range(len(piles)//3):
            output += piles[idx]
            idx += 2
        
        return output
        
        