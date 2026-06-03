# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge case
        if list1 is None: return list2
        elif list2 is None: return list1 

        # head pointer
        head = ListNode()
        temp = head
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next 
                temp = temp.next 

            elif list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
                temp = temp.next

        if list1 is not None:
            temp.next = list1

        if list2 is not None:
            temp.next = list2


        return head.next