from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)

        for i in range(len(s2)- len(s1) +1):
            window = s2[i:i+len(s1)]
            w_count = Counter(window)

            if w_count == s1_count: return True

        return False