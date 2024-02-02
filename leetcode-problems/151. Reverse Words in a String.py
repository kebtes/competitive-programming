class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        word_list = list(s.split())

        left = 0
        right = len(word_list) - 1

        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1

        s = " ".join(word_list)

        return s