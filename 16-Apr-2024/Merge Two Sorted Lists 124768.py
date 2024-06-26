# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        current = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1

            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next