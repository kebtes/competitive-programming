# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        output = float('inf')
        heap = []  
        
        ratio = [[wage[i] / quality[i], quality[i]] for i in range(len(quality))]
        ratio.sort(key=lambda x: x[0])

        total_quality = 0  
        for r, q in ratio:
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                output = min(output, total_quality * r)

        return output
