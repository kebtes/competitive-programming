# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = float('inf')

        def func(speed):
            cnt = 0

            for p in piles:
                cnt += math.ceil(p / speed)

            return cnt <= h

        while l <= r:
            mid = (l + r) // 2

            if func(mid):
                output = min(output, mid)
                r = mid - 1
            else:
                l = mid + 1

        return output