class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0

        i = 0

        while i < len(s) - 1:
            char = s[i]
            if (char == "I" and (s[i+1] == "V" or s[i+1] == "X")) or \
               (char == "X" and (s[i+1] == "L" or s[i+1] == "C")) or \
               (char == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                if s[i+1] == "V":
                    sum += 4
                elif s[i+1] == "X":
                    sum += 9
                elif s[i+1] == "L":
                    sum += 40
                elif s[i+1] == "C":
                    sum += 90
                elif s[i+1] == "D":
                    sum += 400
                elif s[i+1] == "M":
                    sum += 900
                i += 2
            else:
                sum += roman_numerals[char]
                i += 1

        if i == len(s) - 1:
            sum += roman_numerals[s[i]]

        return sum
