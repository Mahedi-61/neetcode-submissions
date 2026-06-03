# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle
        # 2. reverse the second half
        # 3. merge

        #find the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #revese the second half
        a = None
        b = slow.next
        slow.next = None
        while b:
            temp = b.next
            b.next = a
            a = b
            b = temp

        #merge
        while head and a:
            temp = head.next

            head.next = a
            head = head.next
            a = a.next

            head.next = temp
            head = head.next
        
        if a:
            head.next = a

