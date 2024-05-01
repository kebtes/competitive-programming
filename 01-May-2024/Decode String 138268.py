# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                part = ""

                while stack[-1] != "[":
                    part += stack.pop()
                stack.pop()

                mul = ""
                while stack and stack[-1].isdigit():
                    mul = stack.pop() + mul
                
                stack.extend(reversed(part * int(mul)))

        return "".join(stack)



        
            

        