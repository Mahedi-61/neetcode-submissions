# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        sol = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # need to reverse
        b = slow.next
        slow.next = None
        a = None
        while b:
            temp = b.next
            b.next = a
            a = b
            b = temp

        while a:
            temp_s = sol.next
            temp_a = a.next
            
            sol.next = a
            sol.next.next = temp_s
            sol = sol.next.next
            a = temp_a