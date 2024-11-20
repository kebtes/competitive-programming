# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        priority_queue = [(0, src, 0)]

        best_price = defaultdict(lambda: float('inf'))
        best_price[(src, 0)] = 0

        while priority_queue:
            current_price, current_city, current_stops = heapq.heappop(priority_queue)

            if current_city == dst:
                return current_price

            if current_stops > k:
                continue

            for neighbor, weight in graph[current_city]:
                new_price = current_price + weight

                if new_price < best_price[(neighbor, current_stops + 1)]:
                    best_price[(neighbor, current_stops + 1)] = new_price
                    heapq.heappush(priority_queue, (new_price, neighbor, current_stops + 1))

        return -1