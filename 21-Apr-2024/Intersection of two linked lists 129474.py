# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_1 = headA
        ptr_2 = headB
        
        while ptr_1 != ptr_2:
            ptr_1 = headB if not ptr_1 else ptr_1.next
            ptr_2 = headA if not ptr_2 else ptr_2.next
            
        return ptr_1