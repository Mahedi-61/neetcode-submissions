# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(n + m) solution; O(m + n)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        dummy = head 

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(val)
            dummy = dummy.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next