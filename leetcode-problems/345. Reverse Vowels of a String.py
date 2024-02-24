class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1

        s = list(s)
        vowels = "aeiouAEIOU"

        while i < j:
            if s[j] in vowels and s[i] in vowels:
                s[j], s[i] = s[i], s[j]

                j -= 1
                i += 1
                continue

            if s[i] not in vowels:
                i += 1

            if s[j] not in vowels:
                j -= 1


        return "".join(s)