# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        previous = head
        while curr:
            if curr.val == val:
                previous.next = curr.next
                curr = curr.next
            else:
                previous = curr
                curr = curr.next
        if head.val == val:
            return head.next
        else:
            return head
        