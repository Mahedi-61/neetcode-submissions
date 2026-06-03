# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Two pass approach
        curr = head
        total = 1
        while curr.next:
            curr = curr.next
            total += 1

        if total == n:
            return head.next
        else:
            total -= n
            curr = head
            idx = 1

            while curr.next:
                if idx == total:
                    curr.next = curr.next.next
                    idx += 1
                else:
                    curr = curr.next
                    idx += 1

        return head
        


        
