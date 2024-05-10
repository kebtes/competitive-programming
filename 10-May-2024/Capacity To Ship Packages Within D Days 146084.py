# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        output = float('inf')

        def func(capacity):
            turns = 1
            cur_capacity = capacity

            for w in weights:
                if cur_capacity - w < 0:
                    turns += 1
                    cur_capacity = capacity
                
                cur_capacity -= w
            
            return turns <= days


        while l <= r:
            mid = (l + r) // 2

            if func(mid):
                output = min(output, mid)
                r = mid - 1
            else:
                l = mid + 1

        
        return output
            
            