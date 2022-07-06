# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        previous_node, next_node = None,None
        while curr:
            next_node = curr.next
            curr.next = previous_node
            previous_node = curr
            curr = next_node
        return previous_node
    
