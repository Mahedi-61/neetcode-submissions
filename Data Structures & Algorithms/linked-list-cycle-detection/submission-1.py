# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using Floyd's Tortoise & Hare
        # Fast & slow pointer
        if head is None: return False
        slow = head
        fast = head 

        while fast and slow:
            if fast.next is None:
                return False 
                
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False