# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#This is solution using array
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         arr = []
#         for i in range(0,len(lists)):
#             head = lists[i]
#             while head:
#                 arr.append(head.val)
#                 head= head.next
#         arr.sort()    
#         head = ListNode()
#         curr = head
#         for val in arr:
#             new_node = ListNode(val)
#             curr.next = new_node
#             curr = curr.next
#         return head.next
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists)>1:
            mergedList = []
            for i in range(0,len(lists),2):
                mergedList.append(self.merge_two_list(lists[i], lists[i+1] if (i+1) < len(lists) else None))
            lists = mergedList    
        return lists[0]
            
    def merge_two_list(self,list1,list2):
        node = ListNode()
        head = node
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
        return node.next