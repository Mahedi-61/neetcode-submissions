# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp:
            temp = temp.next
            c += 1
        
        
        c = c - n
        if c == 0:
            return head.next
        elif c == 1:
            if head.next is not None:
                head.next = head.next.next
            return head 

        k = 1
        sami = head
        while k < c:
            sami = sami.next
            k += 1

        if sami.next is None:
            pass
        else:
            sami.next = sami.next.next

        return head