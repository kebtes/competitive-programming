# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_part = ListNode(0)
        odd_part = ListNode(0)

        curr = head
        e, o = even_part, odd_part

        i = 0
        while curr:
            if i%2 == 0:
                even_part.next = curr
                even_part = even_part.next
            else:
                odd_part.next = curr
                odd_part = odd_part.next

            curr = curr.next
            i += 1

        odd_part.next = None
        even_part.next = o.next
    
        return e.next
