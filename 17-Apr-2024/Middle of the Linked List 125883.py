# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]):
        lst = []
        curr = head
        cnt = 0

        while curr:
            curr = curr.next
            cnt += 1

        for _ in range(cnt//2):
            head = head.next

        return head
        