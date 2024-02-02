from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        
        m = math.gcd(*(count.values()))
        if m>=2:
            return True

        return False