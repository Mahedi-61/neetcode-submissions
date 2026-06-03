# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pointer approach
        a = None
        b = head 

        while b:
            temp = b.next
            b.next = a
            a = b
            b = temp

        return a 
        