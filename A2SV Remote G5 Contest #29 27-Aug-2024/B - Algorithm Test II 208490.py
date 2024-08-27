# Problem: B - Algorithm Test II - https://codeforces.com/gym/544347/problem/B

from collections import defaultdict, deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insetAfter(self, target_node, new_node):
        if target_node is None:
            # append to the linked list
            
            if self.tail is None: # linked list is empty
                self.head = new_node
                self.tail = new_node

            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

        else:
            new_node.next = target_node.next
            new_node.prev = target_node

            if target_node.next is None: # target node was a tail
                self.tail = new_node
            
            else:
                target_node.next.prev = new_node
            
            target_node.next = new_node

    def removeNode(self, target_node):
        if target_node.prev is None: # if its head
            self.head = target_node.next
            
            if self.head is not None:
                self.head.prev = None
           
            else:
                # this makes the list empty
                self.tail = None

        elif target_node.next is None:
            # check if its tail
            
            self.tail = target_node.prev
            self.tail.next = None # ensures the tail aint pointing to anything

        else:
            # removing nodes in the middle of the list

            target_node.prev.next = target_node.next
            target_node.next.prev = target_node.prev
    
    def __repr__(self) -> str:
        node = self.head
        output = []

        while node:
            output.append(str(node.val))
            node = node.next

        return " ".join(output)

n = int(input())
linked_list = LinkedList()

# nodes hashmap stores multiple instances of nodes with the same value
nodes = defaultdict(deque)

for _ in range(n):
    query = input().split()

    if query[0] == "insert":
        x, y = int(query[1]), int(query[2])

        new_node = Node(x)
        
        # check if node y exists
        if nodes[y]: 
            target_node = nodes[y][0]
            linked_list.insetAfter(target_node, new_node)

        else:
            linked_list.insetAfter(linked_list.tail, new_node)

        nodes[x].append(new_node)

    elif query[0] == "remove":
        w = int(query[1])

        # we check if w exists in our linked list
        if nodes[w]:
            # remove the first occurance of the node in our linked list
            target_node = nodes[w].popleft()
            linked_list.removeNode(target_node)

            # we remove it from our hashmap if there no instances of that node 
            if not nodes[w]: del nodes[w]

print(linked_list)