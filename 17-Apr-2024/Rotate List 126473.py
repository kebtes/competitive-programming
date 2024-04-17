# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 1
        curr = head
        
        while curr.next:
            curr = curr.next
            n += 1
        
        curr.next = head

        steps = n - (k % n)

        for _ in range(steps):
            curr = curr.next

        head = curr.next
        curr.next = None

        return head