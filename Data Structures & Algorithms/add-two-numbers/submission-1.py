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

        while list1 and list2:
            d_sum = list1.val + list2.val + carry
            value = d_sum % 10
            carry = d_sum // 10

            list1.val = value
            list2.val = value

            if list1.next == None or list2.next == None: 
                break
            list1 = list1.next
            list2 = list2.next
            
        if list1.next == None and list2.next == None:
            if carry != 0:
                carry_node = ListNode(carry)
                list1.next = carry_node
            
            list1 = list1.next
            return l1

        elif list1.next is not None and list2.next == None:
            list1 = list1.next
            list2 = list2.next

            while list1:
                d_sum = list1.val + carry
                value = d_sum % 10
                carry = d_sum // 10

                list1.val = value

                if list1.next == None: break
                list1 = list1.next

            if carry != 0:
                carry_node = ListNode(carry)
                list1.next = carry_node
            
            list1 = list1.next
            return l1
            
        elif list2.next is not None and list1.next == None:
            list1 = list1.next
            list2 = list2.next

            while list2:
                d_sum = list2.val + carry
                value = d_sum % 10
                carry = d_sum // 10

                list2.val = value

                if list2.next == None: break
                list2 = list2.next

            if carry != 0:
                carry_node = ListNode(carry)
                list2.next = carry_node
            
            list2 = list2.next
            return l2