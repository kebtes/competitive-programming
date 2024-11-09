# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])
        while queue:
            n = len(queue)
            prev = None

            for _ in range(n):
                current = queue.popleft()

                if prev:
                    prev.next = current
                
                prev = current

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return root