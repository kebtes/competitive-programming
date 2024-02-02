from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = list(text)
        balloon = "balloon"
        count = 0

        while True:
            if len(text) >= len(balloon):
                for char in balloon:
                    if char not in text:
                        return count

                    text.remove(char)
                count += 1
            else: break

        return count