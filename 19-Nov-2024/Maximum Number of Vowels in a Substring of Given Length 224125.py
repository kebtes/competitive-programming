# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        vowels_count = 0

        left = 0
        output = 0
        for right in range(len(s)):
            while (right - left + 1) > k:
                if s[left] in vowels:
                    vowels_count -= 1
                
                left += 1

            if s[right] in vowels:
                vowels_count += 1

            output = max(output, vowels_count)
        
        return output
            


            

        