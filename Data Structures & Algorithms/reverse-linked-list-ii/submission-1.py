# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head 

        begin = ListNode(0)
        idx = 0
        begin.next = head 
        start = begin

        while start.next:
            if idx + 1 != left:
                start = start.next
                idx += 1
            else:
                break

        a = None
        b = start.next

        while b:
            temp = b.next
            b.next = a
            a = b
            b = temp
            idx += 1
            if idx == right:
                break

        start.next = a
        while start.next:
            start = start.next
        start.next = b

        return begin.next