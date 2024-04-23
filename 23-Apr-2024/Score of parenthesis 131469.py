# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        left_braces = 0
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                left_braces += 1
            else:
                left_braces -= 1
                
                if s[i-1] == "(":
                    score += (2 ** left_braces)

        return score