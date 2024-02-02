from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        output = []
        p_counter = Counter(p)

        if len(p) > len(s):
            return []

        for j in range(len(s) - len(p) + 1):
            window = s[j:j + len(p)]
            w_counter = Counter(window)

            if p_counter == w_counter:
                output.append(j)

        return output
        