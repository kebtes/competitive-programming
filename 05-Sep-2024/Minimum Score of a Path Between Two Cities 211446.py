# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        output = float('inf')

        for point_a, point_b, weight in roads:
            graph[point_a].append([point_b, weight])
            graph[point_b].append([point_a, weight])

        queue = deque([1])
        weights = []
        seen = set()
        while queue:
            node = queue.popleft()
            if node in seen: continue

            seen.add(node)
            for neighbor in graph[node]:
                n, weight = neighbor
                queue.append(n)
                weights.append(weight)

        return min(weights)
