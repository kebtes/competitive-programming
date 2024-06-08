# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def check_palindrome(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        def func(i, substring=[]):
            if i >= len(s):
                output.append(substring[:])
                return

            for j in range(i, len(s)):
                if check_palindrome(i,j):
                    substring.append(s[i:j+1])
                    func(j+1)
                    substring.pop()

        func(0)
        return output
