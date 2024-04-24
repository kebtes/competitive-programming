# Problem: Implement Queue Using Stacks - https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        val = self.queue[0]

        self.queue = self.queue[1:]
        return val

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()