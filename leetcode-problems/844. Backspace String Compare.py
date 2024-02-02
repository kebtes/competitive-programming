class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in s:
            if s_stack:
                if i == "#":
                    s_stack.pop()

            if i.isalpha():
                s_stack.append(i)

        for i in t:
            if t_stack:
                if i == "#":
                    t_stack.pop()

            if i.isalpha():
                t_stack.append(i)


        return t_stack == s_stack