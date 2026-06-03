# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pass approach
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            
        k = count - n
        if k == 0:
            return head.next
        
        i = 1
        curr = head
        while curr:
            if i == k:
                curr.next = curr.next.next
            
            curr = curr.next
            i += 1
        return head