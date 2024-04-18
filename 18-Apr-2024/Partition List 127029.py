# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_side = ListNode(0)
        right_side = ListNode(0)

        l, r = left_side, right_side
        curr = head
        
        while curr:
            if curr.val < x:
                left_side.next = curr
                left_side = left_side.next
            else:
                right_side.next = curr
                right_side = right_side.next
            
            curr = curr.next

        right_side.next = None
        left_side.next = r.next

        return l.next
            
        