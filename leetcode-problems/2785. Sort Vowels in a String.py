class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        VOWELS = "aeiou"
        vowels = []

        for ind, char in enumerate(s):
            if char.lower() in VOWELS:
                vowels.append(char)

        vowels.sort()

        i = 0
        for ind, char in enumerate(s):
            if char.lower() in VOWELS:
                s[ind] = vowels[i]
                i += 1

        return "".join(s)