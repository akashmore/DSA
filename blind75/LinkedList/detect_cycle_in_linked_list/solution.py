# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slowPointer = head
        fastPointer = head.next
        while fastPointer and fastPointer.next:
            if slowPointer == fastPointer:
                return True
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return False