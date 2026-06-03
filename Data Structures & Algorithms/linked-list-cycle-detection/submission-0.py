# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head 
        d = {}

        while temp:
            if temp.val in d:
                for i in d[temp.val]:
                    if temp == i:
                        return True
                
                d[temp.val].append(temp)
            else:
                d[temp.val] = [temp]

            temp = temp.next

        return False