class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ok_stack = [0] * len(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    ok_stack[stack.pop()] = 1
                    ok_stack[i] = 1
            else:
                continue

        result = ""
        for i, c in enumerate(s):
            if c in "()":
                if ok_stack[i]:
                    result += c
            else:
                result += c

        return result