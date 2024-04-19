# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        d = output

        num1, num2 = [], []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        num1 = int("".join(map(str, num1)))
        num2 = int("".join(map(str, num2)))

        result = str(num1 + num2)
        
        for num in result:
            new_node = ListNode(num)
            output.next = new_node
            output = new_node

        return d.next



        