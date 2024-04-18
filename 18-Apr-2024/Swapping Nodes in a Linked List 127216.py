# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next

        lst = []
        while curr:
            lst.append(curr)
            curr = curr.next
        
        length = len(lst)

        lst[k-1].val, lst[length-k].val = lst[length-k].val, lst[k-1].val

        return dummy.next 
