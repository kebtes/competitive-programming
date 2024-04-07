# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        journey = [0] * 1001
    
        for cap, start, end in trips:
            journey[start] += cap
            journey[end] -= cap
    
        for num in journey:
            capacity -= num
            if capacity < 0: 
                return False

        return True