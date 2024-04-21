# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        clones = {}

        curr = head
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clones[curr].next = clones.get(curr.next)
            clones[curr].random = clones.get(curr.random)

            curr = curr.next
        
        return clones[head]