class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = int((high - low)/ 2)

        if high%2 == 0 and low%2 == 0:
            return result
        else:
            return result +1