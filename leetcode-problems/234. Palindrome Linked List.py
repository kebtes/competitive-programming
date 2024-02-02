# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        current = head
        lst = []

        while current:
            lst.append(current.val)
            current = current.next

        initial, last = 0, len(lst) - 1

        while initial < last:
            if lst[initial] != lst[last]:
                return False

            initial += 1
            last -= 1
        else: return True