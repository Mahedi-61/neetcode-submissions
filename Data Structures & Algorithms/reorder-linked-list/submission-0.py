# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. do the reverse
        a = None
        b = slow.next
        slow.next = None

        while b:
            nxt = b.next
            b.next = a
            a = b
            b = nxt
        
        # 3. merging
        first = head 
        while a:
            t1 = first.next
            t2 = a.next

            first.next = a
            a.next = t1

            first = t1
            a = t2
