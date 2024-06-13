# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        output = 0

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        for i in range(n):
            for j in range(i+1, n):
                result = len(graph[i]) + len(graph[j])

                if i in graph[j] or j in graph[i]:
                    result -= 1

                output = max(output, result)

        return output