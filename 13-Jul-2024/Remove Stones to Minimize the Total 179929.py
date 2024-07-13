# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            largest = (largest + 1)//2

            heapq.heappush(heap, -largest)
        
        return -sum(heap)

        