# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next

        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        for i in range(1, len(lst)):
            j = i
            while lst[j-1] > lst[j] and j > 0:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                j -= 1

        curr = dummy.next
        for v in lst:
            curr.val = v
            curr = curr.next

        return dummy.next
        
        

        