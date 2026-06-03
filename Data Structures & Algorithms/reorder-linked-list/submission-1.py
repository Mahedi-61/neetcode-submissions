# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. find the middle or middle + 1
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half of the list
        a = None
        b = slow.next 
        slow.next = None 

        while b:
            nxt = b.next
            b.next = a
            a = b
            b = nxt

        # 3. merging tow list
        front = head
        back = a

        while back:
            temp1 = front.next
            temp2 = back.next

            front.next = back
            back.next = temp1 

            front = temp1
            back = temp2
