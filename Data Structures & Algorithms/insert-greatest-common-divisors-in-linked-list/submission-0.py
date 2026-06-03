# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, num1, num2):
        factors = [1]
        less_num = min(num1, num2)
        
        for i in range(2, less_num+1):
            if num1 % i == 0 and num2 % i == 0:
                factors.append(i)

        return factors[-1]

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            val = self.gcd(temp.val, temp.next.val)
            nxt = temp.next
            temp.next = ListNode (val, nxt)
            temp = temp.next.next

        return head 


