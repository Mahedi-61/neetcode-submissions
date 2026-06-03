# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # step 1: finding out where to start reversing

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        idx = 1
        while idx != left:
            prev, curr = curr, curr.next
            idx += 1

        # step 2: reversing the list
        a = None
        while idx != right + 1:
            temp = curr.next
            curr.next, a = a, curr
            curr = temp
            idx += 1

        # updating links
        prev.next.next = curr
        prev.next = a

        return dummy.next 
        

