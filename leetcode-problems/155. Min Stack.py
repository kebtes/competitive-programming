class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min:
            self.min.append(min(
                self.min[-1], val
            ))
        else:
            self.min.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()
        else:
            pass
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()