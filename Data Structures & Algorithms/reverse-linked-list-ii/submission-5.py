# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head

        pos = 1
        curr = head
        rev_head = None
        dummy = ListNode(0)
        final = dummy
        final.next = head

        while curr:
            if pos == left:
                a = None
                b = curr
                prev_split_head = b

                while pos != right + 1:
                    temp = b.next
                    b.next = a
                    a = b
                    b = temp
                    pos += 1

                rev_head = a
                final.next = a
                prev_split_head.next = b
                break
            
            else:
                final = final.next
                curr = curr.next
                pos += 1

        return dummy.next


