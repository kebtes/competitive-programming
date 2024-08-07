# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        output = 0
        n = len(costs) // 2

        for i in range(n):
            output += costs[i][0] + costs[i + n][1]

        return output