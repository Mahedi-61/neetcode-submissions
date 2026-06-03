# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        second = slow.next
        slow.next = None
        a = None

        while second:
            temp = second.next
            second.next = a 
            a = second
            second = temp

        first = head
        second = a

        #merging  
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = first.next.next
            second = temp2
            