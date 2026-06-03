# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(n + m) solution; O(m + n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        dummy = head
        extra = 0

        while l1 and l2:
            val = l1.val + l2.val + extra

            if val > 9:
                extra = 1
                val = val % 10
            else:
                extra = 0

            dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + extra
            if val > 9:
                extra = 1
                val = val % 10
            else:
                extra = 0

            dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next

        while l2:
            val = l2.val + extra
            if val > 9:
                extra = 1
                val = val % 10
            else:
                extra = 0

            dummy.next = ListNode(val)
            dummy = dummy.next
            l2 = l2.next

        if extra != 0:
            dummy.next = ListNode(extra)

        return head.next