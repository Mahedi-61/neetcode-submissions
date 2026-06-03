# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        dummy = ListNode()
        temp = dummy

        while head1 or head2:
            val1 = head1.val if head1 else None
            val2 = head2.val if head2 else None
            if head1 is None:
                temp.next = ListNode(val2)
                head2 = head2.next

            elif head2 is None:
                temp.next = ListNode(val1)
                head1 = head1.next

            else:
                if val1 < val2:
                    temp.next = ListNode(val1)
                    head1 = head1.next

                else:
                    temp.next = ListNode(val2)
                    head2 = head2.next

            temp = temp.next

        return dummy.next
        