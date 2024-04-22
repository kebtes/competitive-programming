# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        closing = {")": "(", "}": "{", "]": "["}
        opening = [char for char in closing.values()]
        stack = []

        for i in s:
            if i in opening:
                stack.append(i)
            
            else:
                if len(stack) == 0:
                    return False
                
                if closing[i] != stack.pop():
                    return False
            
            
        return len(stack) == 0
                