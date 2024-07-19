# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        idx = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]

            if tank < 0:
                tank = 0
                idx = i + 1
        
        return idx
