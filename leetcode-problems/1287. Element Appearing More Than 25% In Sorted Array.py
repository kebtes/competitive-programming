from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = int(len(arr)*0.25)

        count = Counter(arr)
        
        for key, value in count.items():
            if value > freq:
                return key
        