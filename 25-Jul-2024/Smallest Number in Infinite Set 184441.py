# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.values = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.heap:
            val = heapq.heappop(self.heap)
            self.values.discard(val)
            return val
        else:
            smallest = self.current
            self.current += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.values:
            self.values.add(num)
            heapq.heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
