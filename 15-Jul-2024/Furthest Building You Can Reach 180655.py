# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights, bricks, ladders) -> int:
        n = len(heights)
        jumps = []  

        for i in range(n - 1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue

            heapq.heappush(jumps, diff)

            if len(jumps) > ladders:  
                bricks -= heapq.heappop(jumps)

            if bricks < 0:  
                return i

        return len(heights) - 1 
