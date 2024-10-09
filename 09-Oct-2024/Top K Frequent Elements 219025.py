# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # OVERALL TIME COMPLXITY -> k log n
        count = Counter(nums)

        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        
        output = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            output.append(num)

        return output