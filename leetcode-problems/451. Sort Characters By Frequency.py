from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        output = []

        for char in sorted_count:
            output.append(str(char*sorted_count[char]))

        return "".join(output)
