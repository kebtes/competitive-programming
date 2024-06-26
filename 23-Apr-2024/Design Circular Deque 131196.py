# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = []
        self.size = k
        self.current_size = 0

    def insertFront(self, value: int) -> bool:
        if self.current_size >= self.size:
            return False

        self.deque = [value] + self.deque
        self.current_size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.current_size >= self.size:
            return False

        self.deque.append(value)
        self.current_size += 1

        return True

    def deleteFront(self) -> bool:
        if self.current_size <= 0:
            return False

        self.deque = self.deque[1:]
        self.current_size -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.current_size <= 0:
            return False
        
        self.deque.pop()
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        if self.current_size == 0:
            return -1

        return self.deque[0]

    def getRear(self) -> int:
        if self.current_size == 0:
            return -1

        return self.deque[-1]
        
    def isEmpty(self) -> bool:
        return self.current_size == 0
        
    def isFull(self) -> bool:
        return self.current_size == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()