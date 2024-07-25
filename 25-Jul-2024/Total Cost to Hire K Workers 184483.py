# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = 0
        r = len(costs) - 1
        
        left_heap = []
        right_heap = []

        output = 0
        for _ in range(k):
            while len(left_heap) < candidates and l <= r:
                heapq.heappush(left_heap, costs[l])
                l += 1

            while len(right_heap) < candidates and l <= r:
                heapq.heappush(right_heap, costs[r])
                r -= 1

            if not left_heap: heapq.heappush(left_heap, float('inf'))
            if not right_heap: heapq.heappush(right_heap, float('inf'))

            if left_heap[0] <= right_heap[0]:
                output += heapq.heappop(left_heap)
            else:
                output += heapq.heappop(right_heap)

        return output