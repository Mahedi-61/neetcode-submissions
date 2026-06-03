# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(num1, num2):
            if num1 > num2:
                a, b = num1, num2
            else:
                a, b = num2, num1

            while a % b != 0:
                temp = a % b
                a = b
                b = temp
            return  b

        ll = head
        while ll.next:
            val = gcd(ll.val, ll.next.val)
            temp = ll.next
            ll.next = ListNode(val, temp)
            ll = ll.next.next
            
        return head