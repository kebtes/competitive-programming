import operator

class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv
        }
        
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                ans = ops[token](n1, n2)
                stack.append(ans)
        
        return int(stack[0])