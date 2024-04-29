# Problem: Next Greater Node In Linked List - https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        stack = []
        output = [0] * len(lst)

        for i in range(len(lst)):
            while stack and lst[i] > lst[stack[-1]]:
                output[stack.pop()] = lst[i]
            
            stack.append(i)

        return output