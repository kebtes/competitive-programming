# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (fr, to), prob in zip(edges, succProb):
            graph[fr].append((to, prob))
            graph[to].append((fr, prob))

        priority_queue = [(-1, start_node)] # prob, node

        percentage = defaultdict(lambda: float('-inf'))
        percentage[start_node] = 1

        while priority_queue:
            current_prop, current_node = heapq.heappop(priority_queue)
            current_prop = -current_prop

            if current_node == end_node:
                return current_prop

            for neighbor, prob in graph[current_node]:
                new_prop = current_prop * prob

                if new_prop > percentage[neighbor]:
                    heapq.heappush(priority_queue, (-new_prop, neighbor))
                    percentage[neighbor] = new_prop

        return 0 
