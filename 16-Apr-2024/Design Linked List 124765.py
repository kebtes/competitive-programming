# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            current = self.head

            for _ in range(index):
                current = current.next

            if current:
                return current.val
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            current = self.head

            index = self.size - 1

            for _ in range(index):
                current = current.next
            
            current.next = new_node
            self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            new_node = Node(val)
            current = self.head
            index -= 1

            for _ in range(index):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        elif index > 0 and index < self.size:
            current = self.head
            index -= 1

            for _ in range(index):
                current = current.next

            current.next = current.next.next
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)