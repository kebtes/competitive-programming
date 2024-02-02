class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = None
        
        for i, char in enumerate(haystack):
            if char == needle[0]:
                next_word = haystack[i: i + len(needle)]
                if next_word  == needle:
                    index = i
                    return index
        return -1


