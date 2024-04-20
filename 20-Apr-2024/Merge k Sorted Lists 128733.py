# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode(0)
        curr = output
        
        linked = []

        for lst in lists:
            head = lst
            
            while head:
                linked.append(head.val)
                head = head.next

        linked.sort()

        for node in linked:
            new_node = ListNode(node)
            curr.next = new_node
            curr = new_node

        return output.next
        