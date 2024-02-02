from collections import Counter

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good = 0

        for i in range(len(s) - 2):

            word = s[i:i+3]
            count = Counter(s[i:i +3])
            
            if not any(x > 1 for x in count.values()):
                good += 1
        return good