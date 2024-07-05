# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0

        graph = defaultdict(list)
        for idx, route in enumerate(routes):
            for bus_stop in route:
                graph[bus_stop].append(idx)

        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])
        visited_stops.add(source)

        while queue:
            current_stop, level = queue.popleft()

            for bus in graph[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                for stop in routes[bus]:
                    if stop == target:
                        return level + 1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, level + 1))

        return -1
