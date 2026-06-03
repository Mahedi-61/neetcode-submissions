# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = None
        c = 1

        while fast.next:
            if c == n:
                slow = head
            elif c > n:
                slow = slow.next

            fast = fast.next
            c += 1

        if head == fast:
            head = None
            return head

        elif n - c == 0:
            head = head.next
            return head
       
        if slow.next is not None:
            slow.next = slow.next.next
        
        return head