# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        carry = 0
        dummy = ListNode(0)
        temp = dummy

        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            d_sum = val1 + val2 + carry

            value = d_sum % 10
            carry = d_sum // 10

            temp.next = ListNode(value)
            temp = temp.next
            
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return dummy.next
        
