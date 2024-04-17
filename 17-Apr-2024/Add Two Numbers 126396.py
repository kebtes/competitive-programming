# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            result = carry

            if l1:
                result += l1.val
                l1 = l1.next

            if l2:
                result += l2.val
                l2 = l2.next

            carry = result // 10
            new_node = ListNode(result % 10)
            curr.next = new_node
            curr = new_node

            result //= 10

        return dummy.next

