from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1_count = Counter(word1)
        w2_count = Counter(word2)    
        
        if set(word1) != set(word2):
            return False

        w1_count = sorted(w1_count.values())
        w2_count = sorted(w2_count.values())

        return w1_count == w2_count
