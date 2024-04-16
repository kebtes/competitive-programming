# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        lst = []

        while current:
            lst.append(current.val)
            current = current.next

        l, r = 0, len(lst) - 1

        while l < r:
            if lst[l] != lst[r]:
                return False

            l += 1
            r -= 1
        else: return True