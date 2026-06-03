# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        temp.next = head
        count = 0

        while count < left-1:
            temp = temp.next
            count += 1

        a = None
        b = temp.next
        count += 1
        while count <= right:
            nxt = b.next
            a, b.next = b, a
            count += 1
            b = nxt
        temp.next = a 
        while a.next is not None:
            a = a.next
        a.next = b
        return dummy.next
        

