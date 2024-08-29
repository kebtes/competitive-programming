# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [["0"] * 32 for _ in range(len(words))]
        output = 0

        for idx, word in enumerate(words):
            for ch in word:
                order = ord(ch) - ord("a")
                mask[idx][order] = "1"

            mask[idx] = [int("".join(mask[idx]), 2), len(word)]

        for i in range(len(mask)):
            for j in range(i + 1, len(mask)):
                
                if (mask[i][0] & mask[j][0]) == 0:
                    output = max(output, mask[i][1] * mask[j][1])

        return output